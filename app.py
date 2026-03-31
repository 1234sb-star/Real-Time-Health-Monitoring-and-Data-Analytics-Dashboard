from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def generate_data():
    return {
        "heart_rate": random.randint(60, 110),
        "steps": random.randint(1000, 8000),
        "calories": random.randint(150, 600)
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(generate_data())

# 👇 हे NEW add कर
@app.route("/analytics")
def analytics():
    return render_template("analytics.html")

@app.route("/report")
def report():
    return render_template("report.html")

# 👇 हे already आहे (keep it)
if __name__ == "__main__":
    app.run(debug=True)