import spacy
nlp = spacy.load("en_core_web_sm")

#Listing list is a list of dictionaries
def sort_list_by_best(listing_list, user_prefs):

    #Vectorize user query
    query = concatenate_strings(user_prefs)
    vect_query = vectorizer(query)

    #Turn listings into list of vectorized descriptions
    all_listings = [] #list of strings

    for listing in listing_list:
        complete_description = concatenate_strings(listing_list)
        vect_complete_description = vectorizer(complete_description)




    return sorted_list

#user_prefs is dictionary of strings, turn it into one big string
def concatenate_strings(dictionary):
    result = ""
    for value in dictionary.values():
        result += value

    return result

#Turn big string into vector
def vectorizer(query):
    doc = nlp(query)

    entity_vectors = []

    for ent in doc.ents:
        if ent.has_vector:
            entity_vectors.append(ent.vector)
    return entity_vectors
