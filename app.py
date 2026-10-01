from flask import Flask, render_template, request
import requests

import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

API_KEY=os.getenv("API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 404:
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
        else:
            weather = "error"

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)