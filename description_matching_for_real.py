from sentence_transformers import SentenceTransformer, util
import torch

def match_desc(user_desc, apt_data):
    web_descs = []

    # Loop through the list of dictionaries and extract descriptions
    for apt in apt_data:
        desc = apt.get("description", "")  # Get the description from the dictionary, "" if empty
        web_descs.append(desc)  # Append the description of each apt to the list
    
    user_emb = model.encode(user_desc, convert_to_tensor=True)  # Vectorize user_desc

    website_embs = []

    for desc in web_descs:  # Go through each string desc of each apt and convert each to vector then add to list of desc embeddings of each apt
        web_desc_emb = model.encode(desc, convert_to_tensor=True)
        website_embs.append(web_desc_emb)

    # Convert the list of embeddings to a 2D tensor
    website_embs = torch.stack(website_embs)

    similarity_scores = util.pytorch_cos_sim(user_emb, website_embs).squeeze()  # Stores a tensor of cosine similarity scores between user input and house desc

    # Get the indices of the top 10 similarity scores
    top_10_indices = torch.topk(similarity_scores, k=10).indices.tolist()

    # Fetch the corresponding dictionaries from apt_data
    top_10_apartments = [apt_data[idx] for idx in top_10_indices]

    return top_10_apartments
