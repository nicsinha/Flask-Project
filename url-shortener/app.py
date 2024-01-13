from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    #return "Hello Flask !!"
    #here name is jinja var.
    return render_template('home.html')

@app.route('/your-url')
def your_url():
    return render_template('your-url.html',name = request.args['code'])


if __name__ == '__main__':
    app.run(debug=True)