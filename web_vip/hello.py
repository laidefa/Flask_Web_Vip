# coding=utf-8
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask
from flask_bootstrap import  Bootstrap
from  flask_moment import Moment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

moment = Moment(app)
bootstrap=Bootstrap(app)

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required,Length

class NameForm(Form):
    name = StringField('输入播放地址：', validators=[Required()])
    submit = SubmitField('立即播放', validators=[Required()])
from datetime import datetime

from flask import  render_template, session, redirect, url_for, flash

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Video analysis successful, welcome to watch..')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'))




@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




if __name__ == '__main__':
    #测试调试模式(windows)
    #app.run(host="0.0.0.0",debug=True)
    
    
    #线上正式模式(linux)
    b = True
    while (b):
        try:
            app.run(host='0.0.0.0',port='1518')
            b = False
        except:
            k = 0
