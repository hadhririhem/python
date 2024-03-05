from flask import Flask, render_template

app=Flask(__name__)
@app.route("/display/<int:x>/<int:y>/<color1>/<color2>")
def display(x,y,color1,color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)
if __name__=="__main__": 
    app.run(debug=True)