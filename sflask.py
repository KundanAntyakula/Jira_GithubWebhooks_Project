from flask import Flask
app = Flask(__name__) #creating flask app instance

@app.route("/") # decorator purpose is before invoking function it perform action
#if someone is working on API but before he needs to be authenticated so decorator can be used in such circumstances
#similarly here if someone wants to access this hello API are they trying to access on particular path or not
def fl():
    return "first flask"

app.run('0.0.0.0')
#to build we need server but flask has inbuilt development server without deploying on tomcat or bla bla