# import "packages" from flask
from flask import Flask, render_template, request
from flask import Blueprint, render_template
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
import json
import requests

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")



@app.route('/stub/')
def Stub():
    return render_template("stub.html")

@app.route('/zachgreet', methods=['GET', 'POST'])
def zachgreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("zachary_greet.html", name=name)
    # starting and empty input default
    return render_template("zachary_greet.html", name="World")

@app.route('/ethangreet', methods=['GET', 'POST'])
def ethangreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("ethangreet.html", name=name)
    # starting and empty input default
    return render_template("ethangreet.html", name="World")

@app.route('/leo', methods=['GET', 'POST'])
def leo():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("leo.html", name=name)
    # starting and empty input default
    return render_template("leo.html", name="World")


@app.route('/stanley', methods=['GET', 'POST'])
def stanley():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("stanley.html", name=name)
    # starting and empty input default
    return render_template("stanley.html", name="World")

@app.route('/Mini-labs/')
def video():
    return render_template("Mini-labs.html")

@app.route('/signedaddition/')
def signedaddition():
    return render_template("signedaddition.html")

@app.route('/binary/', methods = ['GET', 'POST'])
def binary():
    BITS = 4
    if request.method == 'POST':
        BITS =  int(request.form['BITS'])
    # starting and empty input default
    return render_template("binary.html", BITS=BITS)

@app.route('/about_us/')
def about_us():
    return render_template("about_us.html")

@app.route('/wireframe/')
def wireframe():
    return render_template("wireframe.html")

@app.route('/rgb/')
def rgb():
    return render_template('rgb.html', images=image_data())

@app.route("/binaryaddition")
def binaryaddition():
    return render_template("binaryaddition.html")

@app.route("/colorCode")
def colorCode():
    return render_template("colorCode.html")

@app.route("/logicGates")
def logicGates():
    return render_template("logicGates.html")

@app.route("/spaceClick")
def spaceClick():
    return render_template("spaceClick.html")

@app.route("/arcade")
def arcade():
    return render_template("arcade.html")

@app.route("/reviewPageHollowKnight")
def reviewPageHollowKnight():
    return render_template("reviewPageHollowKnight.html")

@app.route("/reviewPageMinecraft")
def reviewPageMinecraft():
    return render_template("reviewPageMinecraft.html")

@app.route("/reviewPageRocketLeague")
def reviewPageRocketLeague():
    return render_template("reviewPageRocketLeague.html")

@app.route("/reviewPageValorant")
def reviewPageValorant():
    return render_template("reviewPageValorant.html")

@app.route("/reviewPageAmongUs")
def reviewPageAmongUs():
    return render_template("reviewPageAmongUs.html")

@app.route("/reviewPageFortnite")
def reviewPageFortnite():
    return render_template("reviewPageFortnite.html")

@app.route("/reviewPageSeaOfThieves")
def reviewPageSeaOfThieves():
    return render_template("reviewPageSeaOfThieves.html")

@app.route("/reviewPage2k21")
def reviewPage2k21():
    return render_template("reviewPage2k21.html")

@app.route("/reviewPageHearthstone")
def reviewPageHearthstone():
    return render_template("reviewPageHearthstone.html")

@app.route("/reviewPagePokemon")
def reviewPagePokemon():
    return render_template("reviewPagePokemon.html")

@app.route("/reviewPageGenshin")
def reviewPageGenshin():
    return render_template("reviewPageGenshin.html")

@app.route("/reviewPageSmashBros")
def reviewPageSmashBros():
    return render_template("reviewPageSmashBros.html")

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("joke.html", joke=response.json())


@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("jokes.html", jokes=response.json())

@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    """
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    """

    return render_template("covid19.html", stats=response.json())

@app.route('/arcadeAPI', methods=['GET', 'POST'])
def arcadeAPI():

    url = "https://free-to-play-games-database.p.rapidapi.com/api/games"

    querystring = {"sort-by":"alphabetical"}

    headers = {
        'x-rapidapi-host': "free-to-play-games-database.p.rapidapi.com",
        'x-rapidapi-key': "810c60410fmshe6c6bf953125c9ep188957jsn0e6dd57091ec"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    output = json.loads(response.text)

    return render_template("arcadeAPI.html", Games=output)

@app.route('/valorantAPI', methods=['GET', 'POST'])
def forniteAPI():
    url = "https://valorant-weapons.p.rapidapi.com/Sidearms"

    headers = {
        'x-rapidapi-host': "valorant-weapons.p.rapidapi.com",
        'x-rapidapi-key': "f843e28f92mshd3de980258688f8p118a28jsn305a11f8326b"
    }

    response = requests.request("GET", url, headers=headers)

    output = json.loads(response.text)

    return render_template("valorantAPI.html", Sidearms=output)

@app.route('/hearthstoneapi', methods=['GET', 'POST'])
def hearthstoneapi():

    url = "https://omgvamp-hearthstone-v1.p.rapidapi.com/cards"

    headers = {
        'x-rapidapi-host': "omgvamp-hearthstone-v1.p.rapidapi.com",
        'x-rapidapi-key': "9222875d6amsh74b0c5c0e1248fep11845cjsncdbaced252cf"
    }

    response = requests.request("GET", url, headers=headers)

    output = json.loads(response.text)

    return render_template("hearthstoneapi.html", Info=output)

@app.route("/tictactoe")
def tictactoe():
    return render_template("tictactoe.html")

@app.route("/gamequiz")
def gamequiz():
    return render_template("gamequiz.html")

@app.route('/pokemongoapi', methods=['GET', 'POST'])
def pokemongoapi():


    url = "https://pokemon-go1.p.rapidapi.com/type_effectiveness.json"

    headers = {
        'x-rapidapi-host': "pokemon-go1.p.rapidapi.com",
        'x-rapidapi-key': "e0ad7aa5d6msh9dce61ba4b05901p1b8266jsn87d4e268c462"
    }

    response = requests.request("GET", url, headers=headers)

    print(response.text)
    return render_template("pokemongoapi.html", stats=response.json())

@app.route('/guessTheNumber', methods=['GET', 'POST'])
def guessTheNumber():
    # submit button has been pushed
    if request.form:
        name = request.form.get("number")
        if len(number) != 0:  # input field has content
            return render_template("guessTheNumber.html", number=number)
    # starting and empty input default
    return render_template("guessTheNumber.html", number="World")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8000)