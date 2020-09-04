from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('./index.html')


@app.route('/home')
def home():
    return redirect('/')


@app.route('/index')
def index():
    return redirect('/')


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
    return render_template('./contact.html')


@app.route('/blog/2020/dogs')
def blog2():
    return 'Dogs'
