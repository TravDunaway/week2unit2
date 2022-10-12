from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
from cdisplayedcupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

@app.route("/")
def home():
    cupcakes = get_cupcakes("displaycupcake.csv")
    return render_template("index.html", cupcakes = cupcakes)
    

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("all_cupcake_orders.html")

@app.route("/new_cupcake/<name>")
def new_cupcake(name):
    cupcake = find_cupcake("displaycupcake.csv", name)

    if cupcake:
        add_cupcake_dictionary("current_order.csv", cupcake=cupcake)
        return redirect(url_for("/cupcakes"))
    else:
        return "Sorry cupcake not found."

@app.route("/one_cupcake/<name>")
def one_cupcake(name):
    cupcake = find_cupcake("displaycupcake.csv", name)

    if cupcake:
        return render_template("one_cupcake.html", cupcake = cupcake)
    else:
        return "Sorry not Sorry."

@app.route("/current_order")
def current_order():
    cupcakes = get_cupcakes("current_order.csv")
    cupcakes_total = []
    cupcake_set = set()

    for cupcake in cupcakes:
        cupcake_set.add((cupcake["name"], cupcake["cost"], cupcakes.count(cupcake)))
    
    return render_template("current_order.html", cupcake = cupcake_set)



if __name__ == "__main__":
    app.run(debug = True, port = 8000, host = "localhost")

