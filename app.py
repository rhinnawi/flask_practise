# import Flask module
from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

# Instantiate Flask object (the app)
app = Flask(__name__)
Bootstrap(app)

# Configure db
db = yaml.load(open('db.yaml')) # used to configure db according to data in .yaml file, named db.yaml
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app) #instantiate MySQL module

'''
App object has a decorator called route
route used to add endpoints ('/<anything>') to application

Need function to handle the decorator

Second paramter is a list of HTTP requests accepted by app. Defaults to GET
'''
@app.route('/', methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO user VALUES(%s)", ['Jonas'])
    mysql.connection.commit()
    num_users = cur.execute("SELECT * FROM user")

    sächsische_dorfer = ['Meißen', 'Freiberg', 'Moritzburg', 'Radebeul']
    if request.method == 'POST': 
        return request.form['password']
        #return 'Successfully registered!'
    return render_template('index.html', dörfer=sächsische_dorfer) # rendered index.html 
    '''
    url_for can construct URLs for other routes
    uses their function as the argument
    returns a string with the URL ending

    to redirect to actual page, use redirect module
    '''  
    # return redirect(url_for('about'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/css')
def css():
    return render_template('css.html')

# Allows this to be the file that gets executed
if __name__ == '__main__':
    #app.run()
    '''
    port parameter specifies which port server is listening on
    defaults to 5000

    debug saves us from restarting server each time
    '''
    app.run(debug=True, port=5000) 