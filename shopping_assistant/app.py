from flask import Flask, render_template, request, jsonify
from serp_api import search_products

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form["query"]
    products = search_products(query)
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True) 