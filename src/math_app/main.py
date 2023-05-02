# Dependencies live at the top of each file
from flask import Flask, jsonify, request
# Locally defined modules can come in multiple forms
from lib.math import Addition, Division
import lib.math_alt as Math
import lib.math as SuperMath

# Variables with underscores:
# Single underscore _ indicates to other devs that the variable/method is intended to be used privately - but is not enforced
# Double underscores __ are private methods/variables (due to something called 'Name Mangling'). 
# Note they aren't truly private, but this is the approach taken with Python.
# In the case below, this is prepopulated by Python depending on how the server is launched.
app = Flask(__name__)

# Defining endpoints (Methods must be defined prior to use)
@app.route("/")
def healthcheck():
    return jsonify(status="online")

@app.route('/add', methods = ["POST"])
def add_values():
    val1 = request.form['val1']
    val2 = request.form['val2']
    m = SuperMath.Math().AddTwoValues(val1, val2)
    math = m.AddTwoValues()
    math2 = Math.AddTwoValues(val1, val2)
    return jsonify(math=math,math2=math2)

@app.route('/divide', methods = ["POST"])
def divide_values():
    val1 = request.form['val1']
    val2 = request.form['val2']
    result = ''
    math = Division(val1, val2, result)
    math.DivideBy()
    math2 = Math.AddTwoValues(val1, val2)
    return jsonify(math=math,math2=math2)

# Launching the actual server
if __name__ == "__main__":
    app.run()