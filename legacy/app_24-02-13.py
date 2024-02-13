import os
import random
from flask import Flask, render_template, redirect, request, session, jsonify
from flask_session import Session

import openai 
from openai import OpenAI
from openai.types import Image, ImagesResponse
from decouple import config, Config


app = Flask(__name__)
app.secret_key = 'your_secret_key'

# OpenAI config 
config = Config('.env')
API_KEY = config('API_KEY', default='your_api_key')
client = OpenAI(api_key = API_KEY)


## Initialise Variables
# Character attributes
character = {
    "first_name" : "None",
    "last_name": "None",
    "gpt_name": "None",
    "alignment": "None",
    "race": "None"
}

# Genres
genres = [
    'Fantasy',
    'Sci-Fi',
    'Eldritch Horror',
    'Western',
    'Dark Academia',
    'Romantasy',
    'Modern day',
    'Victorian gothic'
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


## Generate Name using ChatGPT
def generate_character_name(genre, first_initial, last_initial):

    prompt = f"I am playing a tabletop RPG game with a {genre} theme. Please generate a name for my character. The first name should begin with the letter {first_initial} and the last name should begin with the letter {last_initial}. Please only write the name itself -- do not write 'First Name:' or 'Last Name:'"

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}], 
        stream = False
    )

    gpt_name = response.choices[0].message.content
    print("GPT Name:", gpt_name)

    return gpt_name
    

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


@app.route('/', methods=['GET', 'POST'])
def index():
    # """Generate Character"""
    
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

    return render_template("index.html", character=character, checkbox_states=checked_attributes, genres=genres, gpt_name=character['gpt_name'], races=races)


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
    
    genre = request.form['genre']
    character['first_name'] = roll_first_name()
    character['last_name'] = roll_last_name()
    character['alignment'] = roll_alignment()
    character['race'] = roll_race()
    character['gpt_name'] = generate_character_name(genre, character['first_name'], character['last_name'])

    return render_template("index.html", character=character, checkbox_states=checked_attributes, genres=genres, gpt_name=character['gpt_name'], races=races)



## ==== PORTRAIT GENERATION ====
@app.route('/generate-portrait', methods=['POST'])
def generate_portrait(genre, gpt_name, alignment, race):

    dalle = client.images.generate(
        model = "dall-e-3",
        prompt = f"I am playing a game with a {genre} theme. Please generate a portrait of a character called {gpt_name}. Their alignment is {alignment} and their race is {race}. The alignment and race should influence how the character looks, but should not be written as text on the image. There should be no text on the image.",
        size = "1024x1024",
        quality = "standard",
        n = 1,
    )

    image_url = dalle.data[0].url

    print(image_url)
    
    return render_template("index.html", character=character, checkbox_states=checked_attributes, genres=genres, gpt_name=character['gpt_name'], image_url=image_url, races=races)


# For saving custom names entered by the user on the character sheet
# @app.route('/update-name', methods=['POST'])
# def update_name():
#     data = request.json
#     # Update the name based on 'type' and 'name' in 'data'
#     if data['type'] == 'first':
#         character['first_name'] = data['name']
#         print("First name updated:", character['first_name'])
#     elif data['type'] == 'last':
#         character['last_name'] = data['name']
#         print("Last name updated:", character['last_name'])
#     # Save the update to your character object or database as needed
#     return jsonify(success=True)


# For updating the Character Sheet Title with the GPT generated name
# @app.route('/update-gpt-name')
# def update_gpt_name():
#     # Assume character['gpt_name'] has been updated with the generated name
#     return jsonify(character=character)

if __name__ == '__main__':
    app.run(debug=True)
