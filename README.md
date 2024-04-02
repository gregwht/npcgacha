![A vector illustration of a yellow gachapon capsule](https://github.com/gregwht/npcgachapon/blob/main/static/img/NPC%20Gachapon%20Header.png)
---
**NPC Gachapon** is an NPC generator for tabletop roleplaying games, utilising a Flask backend written in Python, and a frontend built with HTML, CSS, Bootstrap, Jinja, Javascript, and AJAX.

To use the web app, please visit [npcgachapon.com](https://www.npcgachapon.com) 

Video Demo:  https://youtu.be/rfF0KVVOsiw

To run NPC Gachapon locally, please follow the instructions below.


## Installation
First, clone the NPC Gachapon repo to your computer:

```
git clone https://github.com/gregwht/npcgacha.git
```

Dependencies are listed in `requirements.txt`, and can be installed with the following command:
```
cd npcgacha
pip install -r requirements.txt
```

## Configuration
NPC Gachapon has the optional ability to connect to OpenAI's API in order to generate character names and portrait images using ChatGPT and Dall-E.

In order to make use of this ability, you will have to add your own API key. Visit `https://platform.openai.com/api-keys` and generate an API key for NPC Gachapon, or use an existing key.

In the root directory, create a file called `.env`. Inside of it, type `API_KEY=` followed by your API key. It should look something like the following:
```
API_KEY=abcdefg123456789
```
If you attempt to use the features of NPC Gachapon which make calls to the OpenAI API, namely generating full names or portrait images, without configuring your API key you will receive an error.


## How To Run
From within the root directory, run NPC Gachapon with the following command:
```
python app.py
```
This will provide you with a URL at which you can access the app, usually: `http://127.0.0.1:5000`.
