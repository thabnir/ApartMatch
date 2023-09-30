import csv
import string

import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

valid_letters = string.ascii_lowercase
invalid_letters = "D, F, I, O, Q, U".lower().split(", ")
for i in invalid_letters:
    valid_letters = valid_letters.replace(i, "")

with open("walkscore.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["FSA", "Walk Score", "Transit Score", "Bike Score"])
    for i in range(1, 10):
        for j in string.ascii_lowercase.replace("D", ""):
            fsa = f"h{i}{j}"
            response = requests.get(f'https://www.walkscore.com/score/{fsa}', headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                imgs = soup.find_all("img")
                walk_score = 0
                transit_score = 0
                bike_score = 0
                for img in imgs:
                    alt = img.get("alt")
                    if alt is not None:
                        if "Walk Score of" in alt:
                            walk_score = int(img.get("src").split("/")[-1].split(".")[0])
                        if "Transit Score of" in alt:
                            transit_score = int(img.get("src").split("/")[-1].split(".")[0])
                        if "Bike Score of" in alt:
                            bike_score = int(img.get("src").split("/")[-1].split(".")[0])
                print(fsa, walk_score, transit_score, bike_score)
                csvwriter.writerow([fsa, walk_score, transit_score, bike_score])
