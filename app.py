import os
import random
from flask import Flask, render_template, redirect, request, session, jsonify
from flask_session import Session

import openai
from decouple import Config


app = Flask(__name__)
app.secret_key = 'your_secret_key'


## Initialise Variables
character = {
    "first_name" : "None",
    "last_name": "None",
    "alignment": "None",
    "race": "None"
}

# Default list of races - does not change
races_default = ['Dragonborn', 
            'Dwarf', 
            'Elf', 
            'Gnome', 
            'Half-Elf', 
            'Halfling',
            'Half-Orc',
            'Human',
            'Tiefling']
# Copy races_default into variable called `races`. This is the list of races for the user and can be added to or removed from
races = list(races_default)

checked_attributes = {
    "first_name" : "checked",
    "last_name": "checked",
    "alignment": "checked",
    "race": "checked",
    "portrait": "unchecked"
}


## Roll First Name
def roll_first_name(reroll=False, prev_first=None):
    
    # If rerolling, ensure the new result is not the same as the previous result
    if reroll and prev_first is not None:
        while True:
            # Generate a random uppercase letter for first name
            ascii = random.randint(ord('A'), ord('Z'))
            first_name = chr(ascii)
            # If new letter is different from the previously rolled letter, convert it to char
            if first_name != prev_first:
                break

    else:
        # Generate a random uppercase letter for first name
        ascii = random.randint(ord('A'), ord('Z'))
        first_name = chr(ascii)

  
    # # Print name results:
    # print("First Name:", first_name)
    return first_name


## Roll Last Name
def roll_last_name(reroll=False, prev_last=None):

    # If rerolling, ensure the new result is not the same as the previous result
    if reroll and prev_last is not None:
        while True:
            # Generate a random uppercase letter for first name
            ascii = random.randint(ord('A'), ord('Z'))
            last_name = chr(ascii)
            # If new letter is different from the previously rolled letter, convert it to char
            if last_name != prev_last:
                break

    else:
        # Generate a random uppercase letter for last name
        ascii = random.randint(ord('A'), ord('Z'))
        last_name = chr(ascii)

    # # Print name results:
    # print("Last Name: ", last_name)
    return last_name
    

## Roll Alignment
def roll_alignment(reroll=False, prev_alignment=None):

    if reroll and prev_alignment is not None:
        while True:
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

            if alignment != prev_alignment:
                break

    else:
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
    
    # # Print alignment
    # print("Alignment: ", alignment)
    return alignment


## Roll Race
def roll_race(reroll=False, prev_race=None):
    
    if reroll and prev_race is not None:
        while True:
            # Select a race by rolling a number between 0 and the length of the races list
            race = random.choice(races)
            if race != prev_race:
                break

    else:
        # Select a race by rolling a number between 0 and the length of the races list
        race = random.choice(races)

    # # Print race
    # print("Race:      ", race)
    return race

## Generate Portrait
def generate_portrait():
    print("Generate portrait")
    return


@app.route('/', methods=['GET', 'POST'])
def index():
    # """Generate Character"""
    # global checked_attributes
    
    # If a button is clicked...
    if request.method == 'POST':
        # ...determine what needs to happen.

        ## ==== RACES ====
        # ADD CUSTOM RACE
        global races
        # If a custom race has been submitted by the user...
        if 'custom-race' in request.form:
            # ...store it in the variable new_race
            new_race = request.form['custom-race']
            # If this new race is not already in our list of races, add it
            if new_race and new_race not in races:
                races.append(new_race)

        # RESTORE DEFAULT RACE LIST
        if 'restore-races' in request.form:
            races = list(races_default)


        ## ==== RE-ROLLING ====
        # If re-rolling a specific attribute:
        if 'reroll-attribute' in request.form:
            if request.form['reroll-attribute'] == 'first-name':
                character['first_name'] = roll_first_name(True, character['first_name'])
            elif request.form['reroll-attribute'] == 'last-name':
                character['last_name'] = roll_last_name(True, character['last_name'])    
            elif request.form['reroll-attribute'] == 'alignment':
                character['alignment'] = roll_alignment(True, character['alignment'])
            elif request.form['reroll-attribute'] == 'race':
                character['race'] = roll_race(True, character['race'])

    return render_template("index.html", character=character, races=races, checkbox_states=checked_attributes)


@app.route('/delete-race', methods=['POST'])
def delete_race():

    race = request.form.get('race')
    
    if race in races:
        races.remove(race)
        return redirect("/")
    else:
        return redirect("/")


## ==== CHARACTER GENERATION ====
@app.route('/generate-character', methods=['POST'])
def generate_character():
    # Get the checked attributes and store them in a list. 
    checked_attributes = request.json
    
    # Process the checked attributes and generate the character
    if checked_attributes['first-name'] == 'checked':
        character['first_name'] = roll_first_name()
    if checked_attributes['last-name'] == 'checked':
        character['last_name'] = roll_last_name()
    if checked_attributes['alignment'] == 'checked':
        character['alignment'] = roll_alignment()
    if checked_attributes['race'] == 'checked':
        character['race'] = roll_race()
    if checked_attributes['portrait'] == 'checked':
        generate_portrait()

    print(checked_attributes['first-name'])

    # Return the generated character as JSON response
    return jsonify(character=character, checkbox_states=checked_attributes)



@app.route('/update-name', methods=['POST'])
def update_name():
    data = request.json
    # Update the name based on 'type' and 'name' in 'data'
    if data['type'] == 'first':
        character['first_name'] = data['name']
        print("First name updated:", character['first_name'])
    elif data['type'] == 'last':
        character['last_name'] = data['name']
        print("Last name updated:", character['last_name'])
    # Save the update to your character object or database as needed
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)
