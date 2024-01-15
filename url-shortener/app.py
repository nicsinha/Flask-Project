from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
#This secret_key allow us to securely send messages back and forth from the user make sure that thore trying to
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
        
        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url':request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save('D:\\Git\\Flask-Project\\url-shortener\\static\\user_files\\' + full_name)
            urls[request.form['code']] = {'file':full_name}

        
        with open('urls.json','w') as url_file:
            json.dump(urls,url_file)
    
    
        return render_template('your-url.html',code = request.form['code'])
    else:
        return redirect(url_for('home'))

#Life 51 detect if there is any string after \ in url then store in the code and then pass that code to function.

@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as url_file:
            urls = json.load(url_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url']) 
                else:
                    filename = urls[code]['file']
                    #return redirect(url_for('static', filename='user_files\\' + urls[code]['file'])) 
                    return redirect(url_for('static', filename=f'user_files/{filename}'))


if __name__ == '__main__':
    app.run(debug=True)