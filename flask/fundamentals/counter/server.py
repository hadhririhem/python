from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key = "Keep it secret"

@app.route("/")
def visits() :
    if "count" in session:
        session["count"] += 1 
    else : 
        session["count"] = 0 
    return render_template("counter.html", num = session["count"])

@app.route("/increment")
def increment():
    session["count"] += 2
    return render_template("counter.html")

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

@app.route("/input", methods = ["POST"])
def add_input():
    print(request.form)
    num = request.form["num"]
    session["count"] += int(num)-1
    return redirect("/")


if __name__ == ("__main__"):
    app.run(debug=True)