from flask import Flask

app = Flask("__name__")

@app.route("/")
def home():
    return "<div>I am homepage</div>"

if __name__ == "__main__":
    app.run(debug=True)