import csv
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def hello_world():
    return render_template('./index.html')


@app.route('/about')
def about():
    return render_template('./about.html')


@app.route('/works')
def works():
    return render_template('./works.html')


@app.route('/work')
def work():
    return render_template('./work.html')


@app.route('/contact')
def contact():
    is_submitted = request.args.get('is_submitted')
    if is_submitted:
        return render_template('./contact.html', is_submitted=is_submitted)
    return render_template('./contact.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, 
            delimiter=',', 
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:            
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect(url_for('contact', is_submitted=True))            
        except:
            return 'did not save to database'
    else:
        return 'something went wrong! try again'
