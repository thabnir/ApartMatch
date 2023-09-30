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
    user_data = form.to_dict()
    print("behold, the user data:")
    print(user_data)

    return render_template('tinder.html', user_data=user_data)


if __name__ == '__main__':
    app.run()
