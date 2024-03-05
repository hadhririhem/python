from flask import Flask
app = Flask(__name__)
@app.route('/')
def helloworld():
    return "Hello World!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}"
@app.route('/repeat/<int:int>/<string:string>')
def repeat(int, string):
    return string * int
if __name__=="__main__":
    app.run(debug=True)