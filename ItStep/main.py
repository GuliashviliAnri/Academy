from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("Academy.html")


@app.route("/contacts.html")
def second():
    return render_template("Contacts.html")

@app.route("/about.html")
def third():
    return render_template("About.html")


app.run(debug=True)