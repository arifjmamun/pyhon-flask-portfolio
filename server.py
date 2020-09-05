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


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect(url_for('contact', is_submitted=True))
    else:
        return 'something went wrong! try again'
