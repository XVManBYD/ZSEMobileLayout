import secrets

from flask import Flask, make_response, render_template

app = Flask(__name__, template_folder="static")
app.secret_key = secrets.token_hex()


@app.route("/")
def index():
    return make_response(render_template(template_name_or_list='index.html'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")