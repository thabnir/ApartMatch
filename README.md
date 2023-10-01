### Apartmatch!

Built for the 2023 MAIS Hackathon by Thabnir, flyme2bluemoon, clarallelogram and Rain1618
## Inspiration

As students, we've all faced the dreaded dilemma of finding a place to live next year. Hours wasted scrolling through Facebook, Kijiji, Zumper... and then summoning the courage to chat with real estate agents - it's a nightmare that should be reserved for horror movies, not house hunting! Reading each description and browsing through 20 photos to weed out potentially problematic apartments is time consuming and annoying :angry: . Imagine if you could spend that time cramming for finals instead.

## What it does
Behold, ApartMatch! It gathers listings from various websites into one simple interface. You just input  your budget, the number of bedrooms, and a short description of your dream apartment, and we work our magic. Using image captioning, we analyze the listing photos to provide you with a more truthful description (because let's face it, that third bedroom doesn't always come with windows!). We then combine these enhanced descriptions with the original listing info and employ fancy semantic matching techniques to find your perfect match. One click, and we generate an email to reach out to the listing agent - no more awkward phone calls!

## How we built it
Our backend powered by Flask allowed us to integrate our machine learning models. We fine-tuned a pretrained HuggingFace vit-gpt2-image-captioning model to analyse the listing photos and used bi-encoding to vectorize our descriptions. We chose to use a cosine similarity score to determine how closely a listing matches our dream apartment. Based on the current literature, this appears to be the best metric for our chosen task. The frontend of our website was built with the help of Bootstrap, ChatGPT and lots of tears. 

## Challenges we ran into
Various real estate websites have very different APIs and provides different information. It is quite challenging to integrate them together and merge the listings together in a timely manner.  

## Accomplishments that we're proud of
We are very happy to have built something that we will be able to use next year when we will be apartment-hunting during finals season. Our model to match the user query with the best apartment listing works well!! 

## What we learned
This was the first time we had the opportunity to work with NLP techniques. Throughout the hackathon, we tested a few different models to generate captions and do semantics matching. We were able to gain a better understanding of how each of them worked and how to choose one that is optimable for our use case. We also used Random Forest to build a model that compares the current price of the apartment with similar listings and historical price data to indicate whether or not it is fair. Finally, as none of us had experience with web development before, we all learned a lot and gained a tremendous amount of respect for frontend designers. 

## What's next for ApartMatch
We are hoping to refine the sorting algorithm and include more websites. For our prototype, we have limited ourselves to realtor.ca as it would be very time consuming to integrate all of the different listing websites. Additionally, we would like to improve on the frontend to make it aesthetically more pleasing and integrate more features that would help in the apartment hunting process. For instance, we would like to be able to show all our listings on a map. :rocket: :house_with_garden:
