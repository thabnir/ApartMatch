from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


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

    # do a search function
    apartment_data = [
        {
            'address': '123 Main St',
            'price': 1000,
            'bedrooms': 2,
            'bathrooms': 1,
            'sqft': 1000,
            'profile_image_url': 'https://cdn.realtor.ca/listings/TS638316326049630000/reb5/highres/6/22886256_1.jpg',
            'amenities': ['pool', 'gym', 'parking'],
        },
        {
            'address': '456 Main St',
            'price': 2000,
            'bedrooms': 3,
            'bathrooms': 2,
            'sqft': 2000,
            'profile_image_url': 'https://images.unsplash.com/photo-1605146769289-440113cc3d00?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=3540&q=80',
            'amenities': ['pool', 'no gym sadly :(', 'parking'],
        }
    ]


    return render_template('tinder.html', apartment_data=apartment_data)


if __name__ == '__main__':
    app.run()
