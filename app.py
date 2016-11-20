from flask import Flask, render_template

causes = [
    {
        "name"     : "Women's Health",
        "emoji"    : "peach",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!"
    },
    {
        "name"     : "Immigration Rights",
        "emoji"    : "alien",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!"
    },
    {
        "name"     : "Marriage Equality",
        "emoji"    : "two-women",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!"
    },
    {
        "name"     : "Environmental Issues",
        "emoji"    : "tree",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!"
    },
    {
        "name"     : "Blue Collar Opportunity",
        "emoji"    : "worker",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!"
    },
    {
        "name"     : "Public Policy Research",
        "emoji"    : "microscope",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!"
    },
    {
        "name"     : "Pro-Family Work Policy",
        "emoji"    : "family",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!"
    },
    {
        "name"     : "Education For All",
        "emoji"    : "books",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!"
    },
    {
        "name"     : "Internet Freedom",
        "emoji"    : "connected",
        "why-care" : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "why-now"  : "People have short attention spans, so this bit shouldn't be much longer than a tweet. 170-ish characters works on every screen I tried. Not too short either - think Goldilocks.",
        "more-info": "You know that cool celebrity that everyone loves? What's-his-face from that one movie? Here's something they said that was pro-immigration rights! Yeah! Awesome!",
        "national" : "Here's an example of something a national org needs your money for. Like legislation! A piece of something important that some senator is trying to pass!",
        "local"    : "Here's an example of something a local org needs your money for.  You could be helping someone in your neighborhood!"
    }
]

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', causes=causes)

@app.route('/all-causes')
def all_causes():
    return render_template('all-causes.html', title="All Causes", causes=causes)

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
