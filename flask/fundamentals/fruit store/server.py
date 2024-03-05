from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form['strawberry'])
    print(request.form['raspberry'])
    num_raspberry = request.form['raspberry']
    num_strawberry = request.form['strawberry']
    num_apple = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    count = int(num_apple) + int(num_raspberry) + int(num_strawberry)
    customer_name = first_name + last_name
    print("Charging", customer_name, "for", count, "fruits")
    return render_template("checkout.html", num_apple = num_apple, num_raspberry = num_raspberry, num_strawberry = num_strawberry, 
                            student_id=student_id, last_name=last_name, first_name= first_name, count=count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    