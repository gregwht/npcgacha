import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

## Roll First Name
def roll_first_name():
    # Generate a random uppercase letter for first name
    ascii = random.randint(ord('A'), ord('Z'))
    first_name = chr(ascii)

    # Print name results:
    print("First Name:", first_name)
    return first_name


## Roll Last Name
def roll_last_name():
    # Generate a random uppercase letter for last name
    ascii = random.randint(ord('A'), ord('Z'))
    last_name = chr(ascii)

    # Print name results:
    print("Last Name: ", last_name)
    return last_name


## Roll Alignment
def roll_alignment():
    # Create a variable for lawful vs chaotic
    method = random.randint(0, 2)
    # Create a variable for good vs evil
    morals = random.randint(0, 2)

    # Assign method result
    if method == 0:
        method = "Lawful"
    elif method == 1:
        if morals == 1:
            method = "True"
        else:
            method = "Neutral"
    elif method == 2:
        method = "Chaotic"

    # Assign morals result
    if morals == 0:
        morals = "Good"
    elif morals == 1:
        morals = "Neutral"
    elif morals == 2:
        morals = "Evil"

    # Print alignment
    alignment = method + " " + morals
    print("Alignment: ", alignment)
    return alignment


## Roll Race
def roll_race():
    # Create a list of races
    races = ['Dragonborn', 
            'Dwarf', 
            'Elf', 
            'Gnome', 
            'Half-Elf', 
            'Halfling',
            'Half-Orc',
            'Human',
            'Tiefling']
    # Select a race by rolling a number between 0 and the length of the races list
    race = random.choice(races)
    # Print race
    print("Race:      ", race)
    return race


## Roll Full Character
def roll_character():
    return {
        'first_name': roll_first_name(),
        'last_name': roll_last_name(),
        'alignment': roll_alignment(),
        'race': roll_race()
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    """Generate Character"""

    # If a character has not yet been generated, make one
    if 'character' not in session:
        session['character'] = roll_character()

    character = session['character']

    # If a button is clicked...
    if request.method == 'POST':
        # ...check which button was clicked
        if request.form.get('roll_character'):
            session['character'] = roll_character()
            character = session['character']
            
        elif request.form.get('roll_race'):
            character['race'] = roll_race()
            
    return render_template("index.html", character=character)


if __name__ == '__main__':
    app.run(debug=True)