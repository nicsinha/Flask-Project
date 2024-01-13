from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return "Hello Flask !!"
    #here name is jinja var.
    return render_template('home.html',name = "Nikhil Sinha")

@app.route('/about')
def about():
    return "This is URL shortener !!"


if __name__ == '__main__':
    app.run(debug=True)