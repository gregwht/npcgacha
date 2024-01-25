import random
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

## Initialise Variables
character = {
    "first_name" : "None",
    "last_name": "None",
    "alignment": "None",
    "race": "None"
}

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
    if character['first_name'] == "None":
        character['first_name'] = roll_first_name()
    
    if character['last_name'] == "None":
        character['last_name'] = roll_last_name()
    
    if character['alignment'] == "None":
        character['alignment'] = roll_alignment()

    if character['race'] == "None":
        character['race'] = roll_race()
    

    # If a button is clicked...
    if request.method == 'POST':
        # ...check which button was clicked
        if request.form.get('reroll_attribute') == 'character':
            character['first_name'] = roll_first_name()
            character['last_name'] = roll_last_name() 
            character['alignment'] = roll_alignment()
            character['race'] = roll_race()
            print(character)
        
        elif request.form.get('reroll_attribute') == 'first_name':
            character['first_name'] = roll_first_name()
            print(character)

        elif request.form.get('reroll_attribute') == 'last_name':
            character['last_name'] = roll_last_name()    
            print(character)

        elif request.form.get('reroll_attribute') == 'alignment':
            character['alignment'] = roll_alignment()
            print(character)

        elif request.form.get('reroll_attribute') == 'race':
            character['race'] = roll_race()
            print(character)

    return render_template("index.html", character=character)


if __name__ == '__main__':
    app.run(debug=True)

