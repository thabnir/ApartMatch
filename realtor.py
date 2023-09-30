import json
import logging

import pandas as pd
import requests

cookies = {
    'visid_incap_2269415': '4tvwjL2MSYOojN+pm2zl/1JzGGUAAAAAQUIPAAAAAAB1mlYAL7b/vUi+1jlXvRGQ',
    'nlbi_2269415': 'TG0PQuvJqlYOTs30Z/XrMgAAAADyhBtOJVgTRI0QgnwtafW8',
    'incap_ses_1228_2269415': 'AWCdTmrmsVqxiegukbwKEVJzGGUAAAAAvrhd4fCqCz7BVMRSFB/mTg==',
    'ASP.NET_SessionId': 'snyrf30yz0qhkkznk2suw4uw',
    'visid_incap_2271082': 'BBROOVQ7QUeLZo3m8Dzum1JzGGUAAAAAQUIPAAAAAACK1nIQwfq8Lvly16UYXscN',
    'nlbi_2271082': 'LHOxAux24gNTkyXFVPrQ3QAAAAD1ecJPeN/F0gVTWPbDzE6e',
    'incap_ses_1228_2271082': 'whkEW07OyF4UiugukbwKEVJzGGUAAAAAGWoH/vQhOcu0pzvdzNA5UA==',
    'gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko': 'gigya-pr_ver4',
    'nlbi_2269415_2147483392': 'Ko+wBeHcUQq8oWDeZ/XrMgAAAAAjbX3fdJXjPzwfV0egX7pn',
    'reese84': '3:fxB42R2HoFZZcfZk6Zcz4g==:0DlA9OgnC2J0MXCKLqVAp2NB6/zkkrGJzpibFGiZ3Sthk3ghVn3sc3OTpbRLkOYjn9qnXvbMr/SU9gKYMyJMpogSqBSeXjdHGAtsDUKFxUW0jLm0e91jf4ErCZqhmOmTOWEONqeYh4ABPTEPdtFoyjDyzvgH1aEWiJcMN+fbytOkG5/TJSZn4u/2a387BpDXBzuSzhDnlkT4EK5RiZDeVCbID9Z7CO4gZGl8gfIOcgLsZ3Z9M0ubcZWZsfkFObgLXwHunluQwTiBb63kAZfOhuEfWEE1xAy2ekCk07Wx4PzXhujxsTxnKNbdCxu9n4CxnmLn18mIpVXlhoVa0E1Q1rffRf6LM8eO0GjUvuKxbxv//7p6KhDAmZ9IZAQ5awdg+/ZsMfsU2aigx5Z+WKOkr866nwPebvlMlSpmrcz47zJclqdZgPpdDqSZPD9ppGxp1fMI0BeAtOg9I4gfe+zUqg==:XnT2maI+IF9WjaBQ9+mvnBcT5hz+sRgusJ2NpWMH9m4=',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://www.realtor.ca/',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Connection': 'keep-alive',
}

with open("walkscore.csv", "r") as f:
    walkscore_db = pd.read_csv(f)

def get_listings(page=1):
    data = {
        'ZoomLevel': '10',
        'LatitudeMax': '45.72066',
        'LongitudeMax': '-73.41923',
        'LatitudeMin': '45.32019',
        'LongitudeMin': '-74.011713',
        'Sort': '6-D',
        'PropertyTypeGroupID': '1',
        'TransactionTypeId': '3',
        'PropertySearchTypeId': '0',
        'Currency': 'CAD',
        'RecordsPerPage': '20',
        'ApplicationId': '1',
        'CultureId': '1',
        'Version': '7.0',
        'CurrentPage': f'{page}',
    }
    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', cookies=cookies, headers=headers, data=data)
    if response.status_code == 200:
        r = response.json()
    else:
        with open("realtor.json") as f:
            r = json.loads(f.read())
            print(r)

    results = r["Results"]
    listings = []
    for result in results:
        try:
            print(result)

            postal_code = result["PostalCode"].lower()
            walkscore = walkscore_db[walkscore_db["FSA"] == postal_code[0:3]]
            if walkscore.empty:
                continue

            building = result["Building"]
            property = result["Property"]

            listing = {
                "id": result["Id"],
                "mls": result["MlsNumber"],
                "description": result["PublicRemarks"],
                "size": building["SizeInterior"] if "SizeInterior" in building else building["SizeExterior"],
                "type": building["Type"],
                "agent": result["Individual"][0]["Name"],
                "agentPhone": f'({result["Individual"][0]["Phones"][0]["AreaCode"]}) {result["Individual"][0]["Phones"][0]["PhoneNumber"]}',
                "address": property["Address"]["AddressText"],
                "slug": result["RelativeURLEn"],
                "photo": property["Photo"][0]["HighResPath"],
            }
            listing["bathrooms"] = building["BathroomTotal"] if "BathroomTotal" in building else 0
            listing["bedrooms"] = building["Bedrooms"] if "Bedrooms" in building else 0

            listing["price"] = property["LeaseRentUnformattedValue"]
            listing["parking"] = property["ParkingSpaceTotal"] if "ParkingSpaceTotal" in property else 0

            listings.append(listing)
        except Exception as e:
            logging.error(e)
    return listings

if __name__ == "__main__":
    print(get_listings())
