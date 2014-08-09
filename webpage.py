import os
import  urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
import datetime
from flask import Flask, render_template

app = Flask(__name__)
@app.template_filter()
def datetimefilter(value,format='%Y/%m/%d %H:%M'):
    """covert a datetime to a different format."""
    return value.strftime(format)
app.jinja_env.filters['datetimefilter']=datetimefilter


@app.route("/home")
def home():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5], title="Home", current_time=datetime.datetime.now())

@app.route("/about")
def about():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5], title="About",current_time=datetime.datetime.now())

@app.route("/contact")
def contact():
    return render_template('template.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5], title="Contact Us",current_time=datetime.datetime.now())



if __name__ == '__main__':
    app.run(debug=True)

