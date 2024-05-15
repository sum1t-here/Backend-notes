from flask import Flask

app = Flask(__name__) # create instance of flask class

@app.route('/') # decorator that tells flask what url should trigger the function that follows
def hello():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True) # runs the application on the local devlopment server

    # debug=True : allows error to appear on the webpage