regions = {
    "region_Ahuntsic / Cartierville": "H2B, H2C, H3L, H2M, H2N, H3M, H4J, H4K",
    "region_Anjou": "H1J, H1K",
    "region_Beaconsfield / Baie-D'Urfé": "H9W H9X",
    "region_Côte-St-Luc / Hampstead / Montréal-Ouest": "H4V, H4W, H4X, H3X, H4X, H4B",
    "region_Côte-des-Neiges / Notre-Dame-de-Grâce": "H4A, H4B, H4X, H3S, H3T, H3V, H3W",
    "region_Dollard-Des-Ormeaux": "H9A, H9B, H9G",
    "region_Dorval / L'Île Dorval": "H4S, H4Y, H9P, H9S",
    "region_Griffintown": "H3C",
    "region_Kirkland": "H9J, H9K",
    "region_L'Ile Des Soeurs": "H3E",
    "region_L'île-Bizard / Sainte-Geneviève": "H9C, H9E, H9H",
    "region_LaSalle": "H8N, H8P, H8R",
    "region_Le Plateau-Mont-Royal": "H2H, H2J, H2K, H2L, H2T, H2W, H2X",
    "region_Le Sud-Ouest": "H3C, H4C, H4E, H3J, H3K",
    "region_Mercier / Hochelaga / Maisonneuve": "H1L, H1M, H1N, H1V, H1W",
    "Montréal-Est": "H1B",
    "region_Mont-Royal": "H3P, H3R, H4P",
    "region_Montréal-Nord": "H1G, H1H",
    "region_Outremont": "H2V",
    "region_Pierrefonds / Roxboro": "H8Y, H8Z, H9H, H9K",
    "region_Pointe-Aux-Trembles / Montréal-Est": "H1A, H1B",
    "region_Pointe-Claire": "H9R, H9S",
    "region_Rivière des Prairies": "H1C, H1E",
    "region_Rosemont / La Petite Patrie": "H1T, H1X, H1Y, H2G, H2S",
    "region_Saint-Laurent": "H4L, H4M, H4N, H4R, H4S, H4T",
    "region_Saint-Léonard": "H1P, H1R, H1S",
    "region_Ste-Anne-De-Bellevue": "H9X",
    "region_Verdun": "H3E, H4G, H4H",
    "region_Ville-Marie": "H3A, H5A, H3B, H5B, H3C, H3G, H3H, H2L, H2K, H2Y, H2Z, H4Z",
    "region_Villeray / St-Michel / Parc-Extension": "H3N, H2P, H2R, H1Z",
    "region_Westmount": "H3Y, H3Z"
}

inverted = {}

for region in regions:
    postals = regions[region].split(", ")
    for fsa in postals:
        inverted[fsa.lower()] = region

if __name__ == "__main__":
    print(inverted)
