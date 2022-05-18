import pytz
import requests
import json
from datetime import *

response=requests.get("https://zenquotes.io/api/quotes")

for quote in response.json():
    print(quote)