import random
from flask import Flask, render_template

app = Flask(__name__)


## Name Generation
def roll_name():
    # Generate a random uppercase letter for first and last names
    ascii = random.randint(ord('A'), ord('Z'))
    first = chr(ascii)

    ascii = random.randint(ord('A'), ord('Z'))
    last = chr(ascii)

    # Print name results:
    print("First Name:", first)
    print("Last Name: ", last)

    return first, last


## Alignment Chart
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


## Race Selection
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
    race = races[random.randint(0, len(races))]

    # Print race
    print("Race:      ", race)

    return race


@app.route('/', methods=['GET', 'POST'])
def index():
    """Generate Character"""

    # Roll character attributes
    first, last = roll_name()
    alignment = roll_alignment()
    race = roll_race()

    return render_template("index.html", first=first, last=last, alignment=alignment, race=race)


if __name__ == '__main__':
    app.run(debug=True)