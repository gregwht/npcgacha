# NPC GACHAPON
#### Video Demo:  https://youtu.be/rfF0KVVOsiw
#### Description: NPC Gachapon is an NPC generator for tabletop gaming.
#### Project URL: www.npcgachapon.com

# What the project is
This project came from the desire to have a quick and easy way to come up with non-player characters when running tabletop RPG's like Dungeons & Dragons and Pathfinder. Often players can take unexpected turns, and new non-player characters may need to be created on the fly. Or, when preparing to run gaming sessions, it can be helpful to have a starting point from which you can build NPC characters. NPC Gachapon was built to fill this need.

When you click the Generate Character button, NPC Gachapon will provide you with a starting initial for your NPC's first and last names. These serve as prompts for you to come up with character names that suit your own world. It will also provide a class, race, and alignment for your character. Once this information has been generated, you can alter it however you see fit within the relevant text boxes, or re-roll specific attribuets by clicking their titles.

You have the ability to choose exactly what information NPC Gachapon provides you with. For example, if you only want to generate a first and last initial, you can deselect race, class, and alignment in the settings panel. Furthermore, you can finetune race and class selection: if you only have certain races or classes in mind for your NPC, you can make sure only they are selected.

Where NPC Gachapon gets really interesting is its use of OpenAI's API. This allows you to connect to ChatGPT and Dall-E to fully flesh out your character. Instead of just generating initials, it allows you to generate full names for your character, influenced by gender and game genre. Furthermore, clicking the gachapon capsule will cause Dall-E to generate a portrait image of your character, which can be clicked to view in a new tab.

I hope that this proves useful in helping bring more fleshed-out and numerous NPC characters to your game worlds!


# What the files contain and do
app.py contains the Flask app which handles all of the backend character generation. It contains methods for the following actions:
* Rolling initial
* Rolling alignment
* Rolling race
* Rolling class
* Generating a full name using ChatGPT
* Saving user-submitted attribute information
* Generating a portrait image using Dall-E

config.py was created when configuring OpenAI's API. I'm not sure it's necessary anymore.

There is a .env file which I have not uploaded here, as it contains my API key for the OpenAI API.

Procfile was created when setting up hosting with Heroku and ensures Gunicorn is used.

requirements.txt was also created when setting up hosting with Heroku. It describes the requirements needed to run the web app.

In the templates folder is my index.html file. This contains the HTML frontend of the NPC Gachapon web app.

In the static folder is:
* img folder, containing the images used by my web app.
* js folder, containing the script.js file which contains the javascript. This determines the user interactions available on the frontend, including the submission of user-inputted information to the backend.
* styles.css, which determines how the frontend looks. I also used Bootstrap in the index.html file, so the styles.css file is not as long as it might have been if I hadn't used Bootstrap.

# Debating design choices
One of the major decisions I made was to implement AJAX for submitting information from the frontend to the backend. I was originally just going to use forms like in the Finance task, but that meant the page had to constantly be refreshing and consequently it would lose settings that the user had changed. In order to create a smoother and less-frustrating user-experience I implemented AJAX, allowing settings to persist and a much better overall experience.

One of the main challenges I faced was implementing OpenAI's API. Up until that point I thought NPC Gachapon was okay, but it was quite basic, and could be made more useful. Implementing OpenAI's API really elevated the project into something that is fun to use and can surprise the user in joyful ways.

I had to go through several iterations of the visual design as well. It became clear to me that there should be two sections: one for the character attributes, and one for the settings. I had to experiment with where these should be placed in relation to each other, and their overall style. Then within the character attribteus section, I had to figure out how to juggle the attributes, the Generate Character button, and the gachapon capsuleimage. I initially had a separate button to generate the portrait image, but decided to combine that with the gachapon image itself -- so clicking it will trigger the generation of a portrait. As it takes several seconds for a portrait image to generate, I added visual feedback so the user knew that their interaction had been recognised, and wouldn't keep clicking to generate a portrait. I even disabled the ability to click to generate portraits while a portrait is currently being generated, to avoid multiple unnecessary (and costly) calls to the API.

I also wanted to add a 'help' / info panel which could be viewed if the user needed help using NPC Gachapon, or wanted to learn more about it. I decided to make it a hideable panel instead of putting it at the bottom of the page in order to create a cleaner user experience.
