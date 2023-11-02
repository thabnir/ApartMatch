## Inspiration

As students, we've all faced the dreaded dilemma of finding a place to live next year. Hours wasted scrolling through Facebook, Kijiji, Zumper... and then summoning the courage to chat with real estate agents - it's a nightmare that should be reserved for horror movies, not house hunting! Reading each description and browsing through 20+ photos to weed out potentially problematic apartments is time-consuming and annoying 😡. Imagine if you could spend that time cramming for finals instead.

## What it does
Behold, ApartMatch! It gathers loads of listings listings into one simple interface. You just input your budget, the number of bedrooms and bathrooms you want, and a short text description of your dream apartment, and we work our magic. Using image captioning, we analyze the listing photos to provide you with a more truthful description (because let's face it, that third bedroom doesn't always come with windows!). We then combine these enhanced descriptions with the original listing info and employ fancy semantic matching techniques to find your perfect match. Soon, one click will generate an email to reach out to the listing agent - no more awkward phone calls!

## How we built it
Our Flask-powered backend allowed us to seamlessly integrate our machine learning models into the website. We fine-tuned a pre-trained HuggingFace vit-gpt2-image-captioning model to analyze the listing photos. We then also used a pre-trained PyTorch bi-encoder to vectorize the user's input description of their ideal apartment as well as the descriptions listed on the website. The model then computes cosine similarity scores to determine how closely a listing satisfies the user's dream apartment requirements and displays the top 10 matches.  We built the front end of our website with the help of Bootstrap, ChatGPT, and lots of tears. 

## Challenges we ran into
Various real estate websites have very different APIs and provide different information. It is quite challenging to integrate them together and merge the listings together in a timely manner.  

## Accomplishments that we're proud of
We are very happy to have built something that we will be able to use next year when we will be apartment-hunting during finals season. Our model to match the user query with the best apartment listing works well!! 

## What we learned
This was the first time we had the opportunity to work with NLP techniques. Throughout the hackathon, we tested a few different models to generate captions and do semantics matching. We were able to gain a better understanding of how each of them worked and how to choose one that was optimal for our use case. We also tried to integrate a pre-trained housing price estimation Random Forest model to indicate whether or not a given listing is a fair price but ran out of time before it was finished. Finally, as none of us had experience with web development before, we all learned a lot and gained a tremendous amount of respect for front-end designers. 

## What's next for ApartMatch
We would like to refine the sorting algorithm and include more websites. For our prototype, we have limited ourselves to realtor.ca as it would be very time-consuming to integrate all of the different listing websites. Additionally, we would like to improve on the front end to make it aesthetically more pleasing and integrate more features that would help in the apartment hunting process. For instance, we would like to be able to show all our listings on a map. 🚀 🏡
