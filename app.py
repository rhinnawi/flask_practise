# import Flask module
from flask import Flask

# Instantiate Flask object (the app)
app = Flask(__name__)

'''
App object has a decorator called route
route used to add endpoints ('/<anything>') to application

Need function to handle the decorator
'''
@app.route('/')
def index():
    return "Hello, World!"

# Allows this to be the file that gets executed
if __name__ == '__main__':
    #app.run()
    app.run(debug) #saves us from restarting server each time