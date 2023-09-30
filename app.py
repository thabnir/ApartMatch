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



import requests # library to make http requests to web services

api_key = ""

# input =                 This variable will store text inputted by the user to serve as prompt for GPT-3 to draft an email

def generate_email_content(user_input, api_key): 
    endpoint = 'https://api.openai.com/v1/engines/text-davinci-002/completions' 
    # This stores the URL of the OpenAI API endpoint you want to access which, in this case, is the GPT-3 engine with ID text-davinci-002, which is designed for text generation tasks.
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    # These are HTTP headers required for making the API request. The Authorization header includes your API key for authentication.
    
    data = {
        'prompt': f'Draft an email expressing interest in the apartment located at [Apartment Address]. {user_input}',
        'max_tokens': 300, 
    }
    # This dictionary contains the data to be sent in the API request. It includes a prompt with the user_input appended to it. 
    
    response = requests.post(endpoint, headers=headers, json=data)
    # This line sends an HTTP POST request to the OpenAI API endpoint with the specified headers and data. 
    # It requests the generation of text content based on the provided prompt and user input.

    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['text']
    else:
        print(f"Error: {response.status_code}")
        return None

    # If the API request is successful, it parses the JSON response and returns the generated text from the API's response data.
    # If there's an error, it prints an error message and returns None.

    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    interest = request.form['interest']
    prompt = request.form['prompt']
    
    # Generate the email content using the OpenAI API
    email_content = generate_email_content(prompt)
    
    if email_content:
        # Here, you can send the email using email_content
        # You can also process the interest variable as needed
        return f'Interest: {interest}, Email Prompt: {prompt}, Email Content: {email_content}'
    else:
        return 'Failed to generate email content.'



if __name__ == '__main__':
    app.run()
