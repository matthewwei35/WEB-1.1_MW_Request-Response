
# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<dessert>')
def fave_dessert(dessert):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {dessert} is my favorite animal, too!'

@app.route('/madlibs/<adj>/<noun>')
def madlibs(adj, noun):
    return f'{adj} {noun}'

@app.route('/multiply/<x>/<y>')
def multiply(x, y):
    result = int(x) * int(y)
    return f'{x} times {y} is {result}.'