import os
import random
from flask import Flask, render_template, redirect, request, session, jsonify
from flask_session import Session

### ======== CONFIG ========
# Configure application
app = Flask(__name__)

### ======== INITIALISE VARIABLES ========
# Character attributes
character = {
    "first_initial" : "None",
    "last_initial": "None",
    "gpt_name": "None",
    "alignment": "None",
    "race": "None"
}

# Default list of races - does not change
races_default = [
    'Dragonborn', 
    'Dwarf', 
    'Elf', 
    'Gnome', 
    'Half-Elf', 
    'Halfling',
    'Half-Orc',
    'Human',
    'Tiefling' 
]

# Copy races_default into variable called `races`. This is the list of races for the user and can be added to or removed from
races = list(races_default)

### ======== FUNCTIONS ========

# Roll First Initial
def roll_first_initial():

    # Generate a random uppercase letter for first name
    ascii = random.randint(ord('A'), ord('Z'))
    first_initial = chr(ascii)
    print("First Initial:", first_initial)
    return first_initial


# Roll Last Initial
def roll_last_initial():

    # Generate a random uppercase letter for last name
    ascii = random.randint(ord('A'), ord('Z'))
    last_initial = chr(ascii)
    print("Last Initial: ", last_initial)
    return last_initial


# Roll Alignment
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

    # Set alignment
    alignment = method + " " + morals
    
    # Print alignment
    print("Alignment: ", alignment)
    return alignment


#Roll Race
def roll_race():
    
    # Select a race by rolling a number between 0 and the length of the races list
    race = random.choice(races)

    # Print race
    print("Race:      ", race)
    return race


@app.route('/', methods=['GET', 'POST'])
def index():

    # first_initial = "None"
    # last_initial = "None"

    if request.method == 'POST':


        if request.json['firstInitialChecked']:
            character['first_initial'] = roll_first_initial()
        if request.json['lastInitialChecked']:
            character['last_initial'] = roll_last_initial()
        if request.json['alignmentChecked']:
            character['alignment'] = roll_alignment()
        if request.json['raceChecked']:
            character['race'] = roll_race()

        return jsonify(character)
    
    else:
        return render_template("index.html")
    

if __name__ == '__main__':
    app.run(debug=True)