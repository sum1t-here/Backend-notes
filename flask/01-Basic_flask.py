from flask import Flask

# instantiate flask
app = Flask(__name__)

@app.route("/") #home directory
def hello():
    return "Hello World"

# if you want to run this app you must call the run()
if __name__ == "__main__":
    app.run(debug=True)