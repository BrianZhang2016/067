from flask import request
from flask import render_template
from flask import Blueprint
import json
import requests
from __init__ import app
from crud2.crud_app import app_crud1
from crud2.crud_app import app_crud1
from crud2.app_crud_api import app_crud_api

aboutus = Blueprint('aboutus', __name__)
@aboutus.route('/zachgreet', methods=['GET', 'POST'])
def zachgreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("zachary_greet.html", name=name)
    # starting and empty input default
    return render_template("zachary_greet.html", name="World")

@aboutus.route('/briangreet', methods=['GET', 'POST'])
def briangreet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("briangreet.html", name=name)
    # starting and empty input default
    return render_template("briangreet.html", name="World")

@aboutus.route('/stanley', methods=['GET', 'POST'])
def stanley():
    url = "https://valorant-weapons.p.rapidapi.com/Sidearms"

    headers = {
        'x-rapidapi-host': "valorant-weapons.p.rapidapi.com",
        'x-rapidapi-key': "f843e28f92mshd3de980258688f8p118a28jsn305a11f8326b"
    }

    response = requests.request("GET", url, headers=headers)

    output = json.loads(response.text)

    return render_template("stanley.html", Sidearms=output)

@aboutus.route('/leo', methods=['GET', 'POST'])
def leo():


    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":"32.7157,-117.1611"}

    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': "e0ad7aa5d6msh9dce61ba4b05901p1b8266jsn87d4e268c462"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    output = json.loads(response.text)

    return render_template("leo.html", Weather=output)
