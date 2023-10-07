from flask import Flask, render_template, request, redirect, jsonify
from flask_bootstrap import Bootstrap
import pickle
import pandas as pd

import description_matching_for_real
import caption
import realtor

app = Flask(__name__)
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# Load the Random Forest model
with open("./pricepredict/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)


def predict(input_data, debug=True):
    # should convert the input data of [ [bedrooms], [fsa] ]
    # to a dataframe with columns bedrooms and
    # region_Ahuntsic / Cartierville, region_Anjou, etc.
    num_beds = int(input_data[0][0])
    if debug:
        print(input_data)

    column_names = [
        "bedrooms",
        "region_Ahuntsic / Cartierville",
        "region_Anjou",
        "region_Beaconsfield / Baie-D'Urfé",
        "region_Côte-St-Luc / Hampstead / Montréal-Ouest",
        "region_Côte-des-Neiges / Notre-Dame-de-Grâce",
        "region_Dollard-Des-Ormeaux",
        "region_Dorval / L'Île Dorval",
        "region_Griffintown",
        "region_Kirkland",
        "region_L'Ile Des Soeurs",
        "region_L'île-Bizard / Sainte-Geneviève",
        "region_LaSalle",
        "region_Lachine",
        "region_Le Plateau-Mont-Royal",
        "region_Le Sud-Ouest",
        "region_Mercier / Hochelaga / Maisonneuve",
        "region_Mont-Royal",
        "region_Montréal-Nord",
        "region_Outremont",
        "region_Pierrefonds / Roxboro",
        "region_Pointe-Aux-Trembles / Montréal-Est",
        "region_Pointe-Claire",
        "region_Rivière des Prairies",
        "region_Rosemont / La Petite Patrie",
        "region_Saint-Laurent",
        "region_Saint-Léonard",
        "region_Ste-Anne-De-Bellevue",
        "region_Verdun",
        "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
        "region_Villeray / St-Michel / Parc-Extension",
        "region_Westmount",
    ]

    data = {column_name: False for column_name in column_names}

    # Set the data type of the 'bedrooms' column to integer
    # guess that's not allowed? :(
    data["bedrooms"] = int(input_data[0][0])
    # set the value of the input matching the column name to True
    input_column = input_data[1][0]
    if input_column in data:
        data[input_column] = True

    # Create the DataFrame
    df = pd.DataFrame(data)

    # df = pd.DataFrame(columns=column_names)

    # Create a row with boolean values based on the provided list
    # row_data = [input_data['bedrooms']] + [False] * (len - 1)
    # row_data[column_names.index(input_data['fsa'])] = True
    #
    # # Add the row to the DataFrame
    # df.add(pd.Series(row_data, index=column_names), axis=0)
    # # df.iloc[0] = row_data

    predicted_price = model.predict(df)

    # Return the prediction as JSON response
    prediction = {"predicted_price": predicted_price}
    if debug:
        print(f"Predicted price: {predicted_price}")
    return prediction


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

fsa_map = {
    "h2b": "region_Ahuntsic / Cartierville",
    "h2c": "region_Ahuntsic / Cartierville",
    "h3l": "region_Ahuntsic / Cartierville",
    "h2m": "region_Ahuntsic / Cartierville",
    "h2n": "region_Ahuntsic / Cartierville",
    "h3m": "region_Ahuntsic / Cartierville",
    "h4j": "region_Ahuntsic / Cartierville",
    "h4k": "region_Ahuntsic / Cartierville",
    "h1j": "region_Anjou",
    "h1k": "region_Anjou",
    "h9w h9x": "region_Beaconsfield / Baie-D'Urfé",
    "h4v": "region_Côte-St-Luc / Hampstead / Montréal-Ouest",
    "h4w": "region_Côte-St-Luc / Hampstead / Montréal-Ouest",
    "h4x": "region_Côte-des-Neiges / Notre-Dame-de-Grâce",
    "h3x": "region_Côte-St-Luc / Hampstead / Montréal-Ouest",
    "h4b": "region_Côte-des-Neiges / Notre-Dame-de-Grâce",
    "h4a": "region_Côte-des-Neiges / Notre-Dame-de-Grâce",
    "h3s": "region_Côte-des-Neiges / Notre-Dame-de-Grâce",
    "h3t": "region_Côte-des-Neiges / Notre-Dame-de-Grâce",
    "h3v": "region_Côte-des-Neiges / Notre-Dame-de-Grâce",
    "h3w": "region_Côte-des-Neiges / Notre-Dame-de-Grâce",
    "h9a": "region_Dollard-Des-Ormeaux",
    "h9b": "region_Dollard-Des-Ormeaux",
    "h9g": "region_Dollard-Des-Ormeaux",
    "h4s": "region_Saint-Laurent",
    "h4y": "region_Dorval / L'Île Dorval",
    "h9p": "region_Dorval / L'Île Dorval",
    "h9s": "region_Pointe-Claire",
    "h3c": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h9j": "region_Kirkland",
    "h9k": "region_Pierrefonds / Roxboro",
    "h3e": "region_Verdun",
    "h9c": "region_L'île-Bizard / Sainte-Geneviève",
    "h9e": "region_L'île-Bizard / Sainte-Geneviève",
    "h9h": "region_Pierrefonds / Roxboro",
    "h8n": "region_LaSalle",
    "h8p": "region_LaSalle",
    "h8r": "region_LaSalle",
    "h2h": "region_Le Plateau-Mont-Royal",
    "h2j": "region_Le Plateau-Mont-Royal",
    "h2k": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h2l": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h2t": "region_Le Plateau-Mont-Royal",
    "h2w": "region_Le Plateau-Mont-Royal",
    "h2x": "region_Le Plateau-Mont-Royal",
    "h4c": "region_Le Sud-Ouest",
    "h4e": "region_Le Sud-Ouest",
    "h3j": "region_Le Sud-Ouest",
    "h3k": "region_Le Sud-Ouest",
    "h1l": "region_Mercier / Hochelaga / Maisonneuve",
    "h1m": "region_Mercier / Hochelaga / Maisonneuve",
    "h1n": "region_Mercier / Hochelaga / Maisonneuve",
    "h1v": "region_Mercier / Hochelaga / Maisonneuve",
    "h1w": "region_Mercier / Hochelaga / Maisonneuve",
    "h1b": "region_Pointe-Aux-Trembles / Montréal-Est",
    "h3p": "region_Mont-Royal",
    "h3r": "region_Mont-Royal",
    "h4p": "region_Mont-Royal",
    "h1g": "region_Montréal-Nord",
    "h1h": "region_Montréal-Nord",
    "h2v": "region_Outremont",
    "h8y": "region_Pierrefonds / Roxboro",
    "h8z": "region_Pierrefonds / Roxboro",
    "h1a": "region_Pointe-Aux-Trembles / Montréal-Est",
    "h9r": "region_Pointe-Claire",
    "h1c": "region_Rivière des Prairies",
    "h1e": "region_Rivière des Prairies",
    "h1t": "region_Rosemont / La Petite Patrie",
    "h1x": "region_Rosemont / La Petite Patrie",
    "h1y": "region_Rosemont / La Petite Patrie",
    "h2g": "region_Rosemont / La Petite Patrie",
    "h2s": "region_Rosemont / La Petite Patrie",
    "h4l": "region_Saint-Laurent",
    "h4m": "region_Saint-Laurent",
    "h4n": "region_Saint-Laurent",
    "h4r": "region_Saint-Laurent",
    "h4t": "region_Saint-Laurent",
    "h1p": "region_Saint-Léonard",
    "h1r": "region_Saint-Léonard",
    "h1s": "region_Saint-Léonard",
    "h9x": "region_Ste-Anne-De-Bellevue",
    "h4g": "region_Verdun",
    "h4h": "region_Verdun",
    "h3a": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h5a": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h3b": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h5b": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h3g": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h3h": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h2y": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h2z": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h4z": "region_Ville-Marie (Centre-Ville et Vieux Mtl)",
    "h3n": "region_Villeray / St-Michel / Parc-Extension",
    "h2p": "region_Villeray / St-Michel / Parc-Extension",
    "h2r": "region_Villeray / St-Michel / Parc-Extension",
    "h1z": "region_Villeray / St-Michel / Parc-Extension",
    "h3y": "region_Westmount",
    "h3z": "region_Westmount",
}


# TODO: TRANSLATE OR SUMMARIZE THE DESCRIPTIONS MAYBE
# MANY ARE IN FRENCH
# AND MANY SUCK


@app.route("/search", methods=["GET", "POST"])
def search(debug=True):
    if request.method != "POST":
        return redirect("/")

    count = 20
    user_prefs = request.form.to_dict()
    apt_data = realtor.get_listings(
        page=1,
        count=count,
        rent_max=int(user_prefs["maxPrice"]),
        rent_min=int(user_prefs["minPrice"]),
        beds=bedroom_mapping[user_prefs["beds"]],
        bathrooms=bedroom_mapping[user_prefs["baths"]],
    )

    for apartment in apt_data:
        img_url = apartment["photo"]
        apartment["photo_list"] = realtor.get_listing_images(img_url)

        apartment["address"] = apartment["address"].replace("|", "<br>")
        # convert from numpy.int64 to int
        apartment["walkscore"] = int(apartment["walkscore"])
        apartment["transitscore"] = int(apartment["transitscore"])
        apartment["bikescore"] = int(apartment["bikescore"])

        # remove the (numbers) at the end of the description
        apartment["description"] = apartment["description"].split("(")[0]

        # take the first image and caption it. could choose a random one instead
        # or do all, but that would be slow
        apartment["caption"] = caption.caption_image(
            apartment["photo_list"][0], debug=True
        )

        if apartment["fsa"] not in fsa_map:
            apartment["predicted_price"] = -1
        else:
            apartment["predicted_price"] = -1
            # apartment['predicted_price'] = predict(
            #     [
            #         [
            #             int(apartment['bedrooms']),
            #         ],
            #         [
            #             fsa_map[apartment['fsa']]
            #         ]
            #     ]
            # )

    # test value prediction

    # print apartment predicted prices vs actual prices
    if debug:
        for apartment in apt_data:
            print(
                f"Predicted price: {apartment['predicted_price']}, actual price: {apartment['price']}"
            )

    sorted_data = description_matching_for_real.match_desc(user_prefs["tags"], apt_data)

    return render_template("galleryview.html", data=sorted_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
