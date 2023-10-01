from flask import Flask, render_template, request, redirect, jsonify
from flask_bootstrap import Bootstrap
import pickle

import description_matching_for_real
import realtor

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# Load the Random Forest model
with open('./pricepredict/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    predicted_price = model.predict(input_data)

    # Return the prediction as JSON response
    response = {'predicted_price': predicted_price}
    return jsonify(response)


bedroom_mapping = {
    "ANY": None,
    "ONE": realtor.NumFilter.ONE,
    "ONE_PLUS": realtor.NumFilter.ONE_PLUS,
    "TWO": realtor.NumFilter.TWO,
    "TWO_PLUS": realtor.NumFilter.TWO_PLUS,
    "THREE": realtor.NumFilter.THREE,
    "THREE_PLUS": realtor.NumFilter.THREE_PLUS,
    "FOUR": realtor.NumFilter.FOUR,
    "FOUR_PLUS": realtor.NumFilter.FOUR_PLUS,
    "FIVE": realtor.NumFilter.FIVE,
    "FIVE_PLUS": realtor.NumFilter.FIVE_PLUS,
}


# TODOS FOR TOMORROW:
# MAKE THE SCRAPER PART AT THE END OF SEARCH WORK
# MAKE THE ARROWS ON THE SIDES OF THE SLIDESHOW THING NOT SUCK


# TODO: TRANSLATE THE DESCRIPTIONS
# MANY ARE IN FRENCH (BASTARDS)
# ALSO MANY SUCK
# DO A FILTERING PROCESS?
# MAYBE THAT CAN BE PART OF THE AI CHUNK THAT WE ARE SUPPOSED TO HAVE

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method != "POST":
        return redirect("/")

    count = 20
    user_prefs = request.form.to_dict()
    apt_data = realtor.get_listings(page=1,
                                    count=count,
                                    rent_max=int(user_prefs['maxPrice']),
                                    rent_min=int(user_prefs['minPrice']),
                                    beds=bedroom_mapping[user_prefs['beds']],
                                    bathrooms=bedroom_mapping[user_prefs['baths']])

    for apartment in apt_data:
        img_url = apartment['photo']
        apartment['photo_list'] = realtor.get_listing_images(img_url)

        apartment['address'] = apartment['address'].replace('|', '<br>')
        # convert from numpy.int64 to int
        apartment['walkscore'] = int(apartment['walkscore'])
        apartment['transitscore'] = int(apartment['transitscore'])
        apartment['bikescore'] = int(apartment['bikescore'])

        # remove the (numbers) at the end of the description
        apartment['description'] = apartment['description'].split('(')[0]

    sorted_data = description_matching_for_real.match_desc(user_prefs['tags'], apt_data, count)

    for apt, sorted_apt in zip(apt_data, sorted_data):
        print("apt:")
        print(apt)
        print("sorted_apt:")
        print(sorted_apt)

    return render_template('galleryview.html', data=sorted_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
