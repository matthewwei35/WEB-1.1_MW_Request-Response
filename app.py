# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
  """Shows a greeting to the user."""
  return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
  """Display a message to the user that changes based on their favorite animal."""
  return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
  """Display a message to the user that changes based on their choice of dessert."""
  return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
  """Displays a message to the user based on their choice of adjective and noun."""
  return f'The {adjective} {noun} walked down the road to the candy store.'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
  """Displays the product of two numbers provided by the user."""

  num1 = number1
  num2 = number2

  if num1.isdigit() and num2.isdigit():
    product = int(num1) * int(num2)
    return f'The product of {num1} * {num2} is {product}.'
  else:
    return 'Invalid inputs. Please try again by entering 2 numbers!'

if __name__ == '__main__':
  app.run(debug=True)
