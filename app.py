from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def result():
    
    var_name  = request.form.get('name')
    var_food  = request.form.get('food')
    var_rating  = int(request.form.get('rating'))
    
    # You can validate the car brands. If someone is telling the wrong brand name, reply them with the wrong answer
    
   # value3 = add(value1, value2)
    
    result = {
        'h_name' : var_name,
        'h_food' : var_food,
        'h_rating': var_rating
    }
    
    #return content
    return render_template('index.html', h_result=result)

if __name__ == "__main__":
    app.run(debug=True)
