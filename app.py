import datetime

import requests_cache
from flask import Flask, render_template
import requests
from datetime import *
import pytz
from flask_bootstrap import Bootstrap

app=Flask(__name__)
Bootstrap(app)

current_server_time=datetime.now(pytz.timezone("US/Central"))
server_refresh_time=datetime.combine(date.today(), time(0, 0), pytz.timezone("US/Central"))+timedelta(1)
cache_timeout=server_refresh_time-current_server_time
requests_cache.install_cache("quotes_cache", backend="sqlite", expire_after=cache_timeout)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/daily-quote/")
def get_quote():
    response=requests.get("https://zenquotes.io/api/today/")
    daily_quote=response.json()
    formatted_quote="\"" + daily_quote[0].get("q") + "\"" + " - " + daily_quote[0].get("a")
    return render_template("qotd.html", quote=formatted_quote)


if __name__=="__main__":
    app.run(debug=True)