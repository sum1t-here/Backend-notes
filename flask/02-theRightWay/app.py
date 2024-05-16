from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) # create instance of flask class

@app.route('/') # decorator that tells flask what url should trigger the function that follows
def hello():
    return 'Hello World'

@app.route('/home')
def hello_home():
    return '<h1>Hello from home</h1>'

@app.route('/backend')
def backend():
    return render_template('test.html')

@app.route('/<name>')
def user(name):
    return f'hello {name}'

# redirect to /
@app.route('/redirect')
def url():
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(debug=True) # runs the application on the local devlopment server

    # debug=True : allows error to appear on the webpage