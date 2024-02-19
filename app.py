import os
import random
from flask import Flask, render_template, redirect, request, session, jsonify
from flask_session import Session

from openai import OpenAI
from decouple import config, Config

### ======== CONFIG ========
# Configure application
app = Flask(__name__)

# Configure OpenAI API
config = Config('.env')
API_KEY = config('API_KEY', default='your_api_key')
client = OpenAI(api_key = API_KEY)


### ======== INITIALISE VARIABLES ========
# Character attributes
character = {
    "first_initial" : "None",
    "last_initial": "None",
    "alignment": "None",
    "race": "None",
    "class": "None",
    "gpt_name": "None"
}

# Genres
genres = [
    'Fantasy',
    'Dark Academia',
    'Eldritch Horror',
    'Modern day',
    'Romantasy',
    'Sci-Fi',
    'Victorian gothic',
    'Western'
]

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

# Copy races_default into variable called 'races'. This is the list of races for the user and can be added to or removed from
races = list(races_default)

# Default list of races - does not change
classes_default = [
    'Barbarian',
    'Bard',
    'Cleric',
    'Druid',
    'Fighter',
    'Monk',
    'Paladin',
    'Ranger',
    'Rogue',
    'Sorcerer',
    'Warlock',
    'Wizard' 
]

# Copy classes_default into variable called 'classes'. This is the list of classes for the user and can be added to or removed from
classes = list(classes_default)


### ======== FUNCTIONS ========
# Roll Initial
def roll_initial(previous=None):

    # If rerolling, ensure the new result is not the same as the previous result
    if previous is not None:
        while True:
            # Generate a random uppercase letter
            ascii = random.randint(ord('A'), ord('Z'))
            letter = chr(ascii)
            # If new letter is different from the previously rolled letter, convert it to char
            if letter != previous:
                break

    else:
        # Generate a random uppercase letter
        ascii = random.randint(ord('A'), ord('Z'))
        letter = chr(ascii)

    return letter


# Roll Alignment
def roll_alignment(previous=None):

    if previous is not None:

        print("Previous:", previous)
        
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

            if alignment != previous:
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

    return alignment


# Roll Race
def roll_race(previous=None):

    if previous is not None:
        while True:
            # Select a race by rolling a number between 0 and the length of the races list
            race = random.choice(races)
            if race != previous:
                break

    else:
        # Select a race by rolling a number between 0 and the length of the races list
        race = random.choice(races)

    return race


# Roll Class
def roll_class(previous=None):

    if previous is not None:
        while True:
            # Select a class by rolling a number between 0 and the length of the classes list
            class_ = random.choice(selected_classes)
            if class_ != previous:
                break

    else:
        # Select a class by rolling a number between 0 and the length of the classes list
        class_ = random.choice(selected_classes)

    return class_


# Generate Name using ChatGPT
def generate_gpt_name(genre, first_initial, last_initial):

    prompt = f"I am playing a tabletop RPG game with a {genre} theme. Please generate a name for my character. The first name should begin with the letter {first_initial} and the last name should begin with the letter {last_initial}. Please only write the name itself -- do not write 'First Name:' or 'Last Name:'."

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}],
        stream = False
    )
    gpt_name = response.choices[0].message.content
    print("GPT Name:", gpt_name)

    return gpt_name


### ======== ROUTES ========
@app.route('/', methods=['GET', 'POST'])
def index():
    global selected_classes
    
    if request.method == 'POST':

        if request.is_json:
            request_data = request.get_json()

            # Update list of selected races from frontend
            if request_data.get('checkedRaces'):
                selected_races = request_data.get('checkedRaces')
                print("Checked races:", selected_races)
                if len(selected_races) == 0:
                    selected_races = ['None']

            # Update list of selected classes from frontend
            if request_data.get('checkedClasses'):
                selected_classes = request_data.get('checkedClasses')
                print("Checked classes:", selected_classes)
                if len(selected_classes) == 0:
                    selected_classes = ['None']

            # Handle attribute generation requests
            if request_data.get('firstInitialChecked'):
                character['first_initial'] = roll_initial()
                print("First Initial:", character['first_initial'])
            if request_data.get('lastInitialChecked'):
                character['last_initial'] = roll_initial()
                print(" Last Initial:", character['last_initial'])
            if request_data.get('alignmentChecked'):
                character['alignment'] = roll_alignment()
                print("    Alignment:", character['alignment'] )
            if request_data.get('raceChecked'):
                character['race'] = roll_race()
                print("         Race:", character['race'] )
            if request_data.get('classChecked'):
                character['class'] = roll_class()
                print("        Class:", character['class'] )

            # Handle rerolling of attributes
            reroll_attribute = request_data.get('reroll-attribute')
            if reroll_attribute:
                if reroll_attribute == 'first-initial':
                    character['first_initial'] = roll_initial(character['first_initial'])
                    print("First Initial:", character['first_initial'])
                elif reroll_attribute == 'last-initial':
                    character['last_initial'] = roll_initial(character['last_initial'])    
                    print("Last Initial:", character['last_initial'])
                elif reroll_attribute == 'alignment':
                    character['alignment'] = roll_alignment(character['alignment'])
                    print("Alignment:", character['alignment'])
                elif reroll_attribute == 'race':
                    character['race'] = roll_race(character['race'])
                    print("Race:", character['race'])
                elif reroll_attribute == 'class':
                    character['class'] = roll_class(character['class'])
                    print("Class:", character['class'])

            # Generate GPT
            if request_data.get('gptNameChecked'):
                genre = request_data.get('genreSelected') 
                print("Genre:", genre)
                character['gpt_name'] = generate_gpt_name(genre, character['first_initial'], character['last_initial'])

            # Return updated character attributes as JSON response
            return jsonify(character)
        else:
            return jsonify({'error': 'Invalid request data. Expected JSON data.'}), 400
        
    else:
        return render_template("index.html", races=races, classes=classes, genres=genres)
    

if __name__ == '__main__':
    app.run(debug=True)