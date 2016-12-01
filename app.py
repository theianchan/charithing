from flask import Flask, render_template, request
import requests
import json

causes = [
    {
        "name"     : "Women's Health",
        "emoji"    : "peach",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 1

    },
    {
        "name"     : "Immigration Rights",
        "emoji"    : "alien",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 2
    },
    {
        "name"     : "Freedom of the Press",
        "emoji"    : "detective-6",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 3
    },
    {
        "name"     : "Environmental Issues",
        "emoji"    : "globe",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 4
    },
    {
        "name"     : "Blue Collar Opportunity",
        "emoji"    : "worker-1",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 5
    },
    {
        "name"     : "Civil Rights Preservation",
        "emoji"    : "courthouse",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 6
    },
    {
        "name"     : "Conflicts of Interest",
        "emoji"    : "money",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 7
    },
    {
        "name"     : "Education For All",
        "emoji"    : "books",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 8
    },
    {
        "name"     : "Internet Rights",
        "emoji"    : "lock",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 9
    }
]

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", causes=causes)

@app.route("/all-causes")
def all_causes():
    return render_template("all-causes.html", title="All Causes", causes=causes)

@app.route("/search")
def search():
    selected = request.args.get("cause")
    results = ""

    if selected:
        url = "http://api.charitynavigator.org/api/v1/search"
        querystring = {
            "category": selected,
            "app_key" :"73973e687b179c033a5a40981816be38",
            "app_id"  :"1b9235b1"
        }
        headers = {
            "cache-control": "no-cache",
            "postman-token": "8511474e-ec22-6f90-554a-b1b541c627d7"
        }
        response = requests.request("GET", url, headers=headers, params=querystring).text
        results = json.loads(response)
        results = results["objects"][:3]

        # TODO
        # check if response is 200 before processing response

    return render_template(
        "search.html", title="Results",
        causes=causes, selected=selected, results=results
    )

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
