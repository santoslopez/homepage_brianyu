import os

from flask import abort, Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/music50")
def music50():
    return render_template("music.html")

# Custom Routing
# Adapted from https://github.com/cs50/ly50

routes = {}
with open("data/routes.txt") as f:
    for line in f:

        # Make sure the line is valid.
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            path, location = line.split()
        except ValueError:
            continue
        path = path.lower()
        if not path.startswith("/"):
            path = "/{}".format(path)
        routes[path] = location

@app.route("/<path:path>")
def reroute(path):
    path = "/{}".format(path.lower())
    if path in routes:
        return redirect(routes[path])
    abort(404)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
