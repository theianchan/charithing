import os
import sqlite3
import requests
import json
import urllib

from flask import Flask, render_template, request, g
from markupsafe import Markup

causes = [
    {
        "name": "Women's Health",
        "emoji": "peach",
        "why-care": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 12
    },
    {
        "name": "Immigration Rights",
        "emoji": "alien",
        "why-care": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 21
    },
    {
        "name": "Freedom of the Press",
        "emoji": "detective-6",
        "why-care": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 5
    },
    {
        "name": "Environmental Issues",
        "emoji": "globe",
        "why-care": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 11
    },
    {
        "name": "Blue Collar Opportunity",
        "emoji": "worker-1",
        "why-care": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 29
    },
    {
        "name": "Civil Rights Preservation",
        "emoji": "courthouse",
        "why-care": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 21
    },
    {
        "name": "Conflicts of Interest",
        "emoji": "money",
        "why-care": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 21
    },
    {
        "name": "Education For All",
        "emoji": "books",
        "why-care": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 7
    },
    {
        "name": "Internet Rights",
        "emoji": "lock",
        "why-care": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now": "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
        "cause_id" : 5
    }
]

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "charithing.db"),
    SECRET_KEY="6BvsfCakge9zyH3ByMtBpRJB",
    USERNAME="admin",
    PASSWORD="8hJHnbdrWCfWBKom84EDHLAh"
))
app.config.from_envvar("CHARITHING_SETTINGS", silent=True)


def get_db():
    """Opens a new database connection if there is none yet for the
    current application co\ntext."""
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    db = get_db()
    with app.open_resource("schema.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command("initdb")
def initdb_command():
    """Initializes the database."""
    init_db()
    print "Initialized the database."


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()


def get_causes():
    db = get_db()
    cur = db.execute("select * from causes") # Maybe not correct syntax
    print cur
    causes = cur.fetchall()
    return causes


@app.template_filter('urlencode')
def urlencode_filter(s):
    if type(s) == 'Markup':
        s = s.unescape()
    s = s.encode('utf8')
    s = urllib.quote_plus(s)
    return Markup(s)


@app.route("/")
def index():
    # db = get_db()
    # db.execute("""
    #     ALTER TABLE causes ADD COLUMN
    #         (name TEXT,
    #         emoji TEXT,
    #         why_care TEXT,
    #         why_now TEXT,
    #         more_info TEXT,
    #         national TEXT,
    #         local TEXT,
    #         cause_id INTEGER);
    #     INSERT INTO causes (name, emoji, why_care, why_now, more_info, national, local, cause_id)
    #     VALUES (
    #         "Internet Rights",
    #         "lock",
    #         "People have short attention spans\, so this bit shouldn\'t be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks",
    #         "People have short attention spans\, so this bit shouldn\'t be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks",
    #         "You know that cool celebrity that everyone loves? What\'s-his-face from that one movie? Here\'s something they said that was pro-immigration rights! Yeah! Awesome",
    #         "Here\'s an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass",
    #         "Here\'s an example of something a local org needs your money for.  You could be helping someone in your neighborhood!",
    #         9
    #     );
    #     """)
    # causes = get_causes()
    return render_template("index.html", causes=causes)


@app.route("/all-causes")
def all_causes():
    # causes = get_causes()
    return render_template("all-causes.html", title="All Causes", causes=causes)


@app.route("/search")
def search():
    term = request.args.get("term")
    scope = request.args.get("scope")
    # causes = get_causes()
    results = ""

    if term:
        url = "http://api.charitynavigator.org/api/v1/search"
        querystring = {
            "term"   : term,
            "scope"  : scope,
            "app_key":"73973e687b179c033a5a40981816be38",
            "app_id" :"1b9235b1",
            "limit"  : 5
        }
        headers = {
            "cache-control": "no-cache",
            "postman-token": "8511474e-ec22-6f90-554a-b1b541c627d7"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring
        )

        if response.status_code == requests.codes.ok:
            results = response.json()["objects"]

    return render_template(
        "search.html", title="Results",
        causes=causes, results=results
    )

if __name__ == "__main__":
    app.run(debug=DEBUG, host=HOST, port=PORT)
