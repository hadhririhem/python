from flask import Flask, render_template

app=Flask(__name__)
@app.route("/play/<int:num>/<colour>")
def play(num,colour):
    return render_template("index.html", num=num, colour=colour)
if __name__=="__main__": 
    app.run(debug=True)