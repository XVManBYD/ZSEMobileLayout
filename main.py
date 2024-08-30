import secrets
from calendar import weekday

from django.utils.termcolors import background
from flask import Flask, make_response, render_template

app = Flask(__name__, template_folder="static/HTML")
app.secret_key = secrets.token_hex()


@app.route("/")
def index():
    return make_response(render_template(template_name_or_list='index.html',
                                         weekday="0",
                                         color_schemes=["#9a3d24", "#4abfec", "#643caf", "#4db234", "#c5a217"],
                                         background=[],
                                         app_version="2024.08.1"))


@app.route("/test")
def test():
    return make_response(render_template(template_name_or_list='test.html'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")