import requests
import urllib.request
import argparse

parser = argparse.ArgumentParser(description='Load and save picture in a folder')
parser.add_argument("-s", "--search", type=str, help="enter what you search ", default="sea")
parser.add_argument("-p", "--per_page", type=int, help="enter what you search ", default=10)
args = vars(parser.parse_args())

SEARCH = args['search']
PAGES=args['per_page']

CLIENT_ID = "YOUR CLIENT ID"

req = requests.get(f'https://api.unsplash.com/search/photos/?client_id={CLIENT_ID}&per_page={PAGES}&query={SEARCH}')
req = req.json()

pictures = req["results"]
print(f"You have {len(pictures)} results")
for i in range(len(pictures)):
    print(f"{(i+1)*100/len(pictures)}% loaded")
    fullpath = pictures[i]["urls"]["full"]
    urllib.request.urlretrieve(fullpath,f"pictures/{SEARCH}_{pictures[i]['id']}.png")

