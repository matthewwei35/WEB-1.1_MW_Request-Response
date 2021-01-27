from flask import Flask
import random

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
  
  if number1.isdigit() and number2.isdigit():
    product = int(number1) * int(number2)
    return f'The product of {number1} * {number2} is {product}.'
  else:
    return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
  """Displays a repeated string a given number of times."""
  result = word

  if n.isdigit():
    for i in range(1, int(n)):
      result = result + ' ' + word
  else:
    return 'Invalid input. Please try again by entering a word and a number!'

  return f'{(1 + i)} Repeats: {result}'

@app.route('/dicegame')
def dicegame():
  """Chooses a random number from 1 to 6. If the user rolls a 6, they win the game; otherwise, they lose."""
  random_number = random.randint(1, 6)

  if random_number == 6:
    return f'You rolled a {random_number}. You won!'
  else:
    return f'You rolled a {random_number}. You lost!'

if __name__ == '__main__':
  app.run(debug=True)
