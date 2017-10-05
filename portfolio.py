import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("index.html")
@app.route("/projects")
def projects():
    return flask.render_template("projects.html")
@app.route("/about")
def about():
    return flask.render_template("about.html")
app.run(debug=True)