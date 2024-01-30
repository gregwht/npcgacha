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

  
    # Print name results:
    print("First Name:", first_name)
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

    # Print name results:
    print("Last Name: ", last_name)
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
    
    # Print alignment
    print("Alignment: ", alignment)
    return alignment


## Roll Race
def roll_race(reroll=False, prev_race=None):
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
    
    if reroll and prev_race is not None:
        while True:
            # Select a race by rolling a number between 0 and the length of the races list
            race = random.choice(races)
            if race != prev_race:
                break

    else:
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

    # Track the state of each checkbox
    checkbox_states = {
        'first_name' : 'checked',
        'last_name' : 'checked',
        'alignment' : 'checked',
        'race' : 'checked'
    }

    # If a character has not yet been generated, make one
    if character['first_name'] == "None":
        character['first_name'] = roll_first_name()
    
    if character['last_name'] == "None":
        character['last_name'] = roll_last_name()
    
    if character['alignment'] == "None":
        character['alignment'] = roll_alignment()

    if character['race'] == "None":
        character['race'] = roll_race()
    
    ## ==== RE-ROLLING ====
    # If a button is clicked...
    if request.method == 'POST':
        # ...determine what needs to be re-rolled.

        ## RE-ROLL CHARACTER
        if request.form.get('reroll_attribute') == 'character':
            # Get the checked attributes and store them in a list
            reroll_checked = request.form.getlist('reroll_checkbox')
            print('Checked:', reroll_checked)
            if 'first_name' in reroll_checked:
                character['first_name'] = roll_first_name(True, character['first_name'])
            if 'last_name' in reroll_checked:
                character['last_name'] = roll_last_name(True, character['last_name'])
            if 'alignment' in reroll_checked:
                character['alignment'] = roll_alignment(True, character['alignment'])
            if 'race' in reroll_checked:
                character['race'] = roll_race(True, character['race'])
        

        ## RE-ROLL INDIVIDUAL ATTRIBUTES
        elif request.form.get('reroll_attribute') == 'first_name':
            character['first_name'] = roll_first_name(True, character['first_name'])
            print(character)

        elif request.form.get('reroll_attribute') == 'last_name':
            character['last_name'] = roll_last_name(True, character['last_name'])    
            print(character)

        elif request.form.get('reroll_attribute') == 'alignment':
            character['alignment'] = roll_alignment(True, character['alignment'])
            print(character)

        elif request.form.get('reroll_attribute') == 'race':
            character['race'] = roll_race(True, character['race'])
            print(character)

        # Update checkbox_states based on form submission
        for key in checkbox_states.keys():
            checkbox_states[key] = 'checked' if key in reroll_checked else ''

    return render_template("index.html", character=character, checkbox_states=checkbox_states)


if __name__ == '__main__':
    app.run(debug=True)

