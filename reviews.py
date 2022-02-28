from flask import request
from flask import render_template
from flask import Blueprint
from __init__ import app

reviews = Blueprint('reviews', __name__)

@reviews.route('/reviewSpiderman/')
def reviewSpiderman():
    return render_template("reviewSpiderman.html")

@reviews.route('/reviewJurassicpark/')
def reviewJurassicpark():
    return render_template("reviewJurassicpark.html")

@reviews.route('/reviewStarwarsep6/')
def reviewStarwarsep6():
    return render_template("reviewStarwarsep6.html")

@reviews.route('/reviewDarkknight/')
def reviewDarkknight():
    return render_template("reviewDarkknight.html")

@reviews.route('/reviewTheoffice/')
def reviewTheoffice():
    return render_template("reviewTheoffice.html")

@reviews.route('/reviewBreakingbad/')
def reviewBreakingbad():
    return render_template("reviewBreakingbad.html")

@reviews.route('/reviewSquidgame/')
def reviewSquidgame():
    return render_template("reviewSquidgame.html")

@reviews.route('/reviewMandalorian/')
def reviewMandalorian():
    return render_template("reviewMandalorian.html")

@reviews.route("/reviewPageHollowKnight")
def reviewPageHollowKnight():
    return render_template("reviewPageHollowKnight.html")

@reviews.route("/reviewPageMinecraft")
def reviewPageMinecraft():
    return render_template("reviewPageMinecraft.html")

@reviews.route("/reviewPageRocketLeague")
def reviewPageRocketLeague():
    return render_template("reviewPageRocketLeague.html")

@reviews.route("/reviewPageValorant")
def reviewPageValorant():
    return render_template("reviewPageValorant.html")

@reviews.route("/reviewPageAmongUs")
def reviewPageAmongUs():
    return render_template("reviewPageAmongUs.html")

@reviews.route("/reviewPageFortnite")
def reviewPageFortnite():
    return render_template("reviewPageFortnite.html")

@reviews.route("/reviewPageSeaOfThieves")
def reviewPageSeaOfThieves():
    return render_template("reviewPageSeaOfThieves.html")

@reviews.route("/reviewPage2k21")
def reviewPage2k21():
    return render_template("reviewPage2k21.html")

@reviews.route("/reviewPageHearthstone")
def reviewPageHearthstone():
    return render_template("reviewPageHearthstone.html")

@reviews.route("/reviewPagePokemon")
def reviewPagePokemon():
    return render_template("reviewPagePokemon.html")

@reviews.route("/reviewPageGenshin")
def reviewPageGenshin():
    return render_template("reviewPageGenshin.html")

@reviews.route("/reviewPageSmashBros")
def reviewPageSmashBros():
    return render_template("reviewPageSmashBros.html")

@reviews.route('/movies', methods=['GET', 'POST'])
def reviews():
    return render_template("layouts/movies.html")
