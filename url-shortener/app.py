from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path


app = Flask(__name__)
#This secret_key allow us to securely send messages bach and forth from the user make sure that thore trying to
#snooping on the connection can not see this info. Random key.
app.secret_key = "asdertgcde1279"

@app.route('/')
def home():
    #return "Hello Flask !!"
    #here name is jinja var.
    return render_template('home.html')

@app.route('/your-url',methods=['GET','POST'])
def your_url():
    #In case of get request.
    #return render_template('your-url.html',name = request.args['code'])
    if request.method == 'POST':
        urls = {}

        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)

        if request.form['code'] in urls.keys():
            flash('That short name has already been taken. Please select another name')
            return redirect(url_for('home'))

        urls[request.form['code']] = {'url':request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls,url_file)
    
    
        return render_template('your-url.html',code = request.form['code'])
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)