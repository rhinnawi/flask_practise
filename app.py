# import Flask module
from flask import Flask, render_template, url_for, redirect

# Instantiate Flask object (the app)
app = Flask(__name__)

'''
App object has a decorator called route
route used to add endpoints ('/<anything>') to application

Need function to handle the decorator
'''
@app.route('/')
def index():
    # return render_template('index.html') # rendered index.html 
    '''
    url_for can construct URLs for other routes
    uses their function as the argument
    returns a string with the URL ending

    to redirect to actual page, use redirect module
    '''  
    return redirect(url_for('about'))

@app.route('/about')
def about():
    return render_template('about.html')

# Allows this to be the file that gets executed
if __name__ == '__main__':
    #app.run()
    '''
    port parameter specifies which port server is listening on
    defaults to 5000

    debug saves us from restarting server each time
    '''
    app.run(debug=True, port=5000) 