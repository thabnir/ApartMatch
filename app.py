from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import realtor


app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = request.form
    user_prefs = form.to_dict()
    print("behold, the user data:")
    print(user_prefs)

    # TODO: TRANSLATE THE DESCRIPTIONS
    # MANY ARE IN FRENCH (BASTARDS)

    # do a search function
    apt_data = realtor.get_listings(2)
    apartment_data = [
        {
         'id': '26122566',
         'mls': '26750912',
         'description': 'Luxury Condo at the heart of Montreal.  Near Metro station Green line and Orange line.  Next to Univeristy of Concordia. Step distance to Sainte Catherine street with a lot of restaurant and shops.  High end construction and amenities. Good orientation with a lot of sunshine come in. (52873478)',
         'size': '343 sqft',
         'type': 'Apartment',
         'agent': 'Claire Zhu',
         'agentPhone': '(514) 886-2568',
         'address': '1500 Boul. René-Lévesque O.|#1003|Montréal (Ville-Marie), Quebec H3G0H6',
         'slug': '/real-estate/26122566/1500-boul-rené-lévesque-o-1003-montréal-ville-marie-central-west',
         'photo': 'https://cdn.realtor.ca/listings/TS638316832191670000/reb5/highres/2/26750912_1.jpg',
         'bathrooms': '1',
         'bedrooms': 0,
         'price': '1559',
         'parking': 0
         },
    ]


    return render_template('tinder.html', data=apt_data)


if __name__ == '__main__':
    app.run()
