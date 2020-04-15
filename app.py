import requests
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

def sum_up(list_of_numbers):
    total = 0
    for number in list_of_numbers:
        if type(number) != int and type(number) != float:
            raise TypeError('number in list (' + str(number) +') expect to be int/float, instead was ' + str(type(number)))
        total = total + number
    return(total)

@app.route('/total', methods=['POST'])
def total():
    data = request.get_json()
    print(data['listOfNumbers'])
    list_of_numbers = data['listOfNumbers']
    try:
        total = sum_up(list_of_numbers)
    except TypeError:
        return('Please only use int/floats in your list of numbers', 400)
    except:
        return('Internal server error', 500)
    return{'total':total}