from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    friends = Friend.get_all()
    return render_template("index.html", friends= friends)

@app.route("/create_friend", methods=["POST"])
def create_friend():
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "occ" : request.form["occ"],
    }
    Friend.save(data)
    return redirect("/")

if __name__ == ("__main__") :
    app.run(debug=True)

