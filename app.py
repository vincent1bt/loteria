import random
import os
from flask import Flask, render_template, request, session, redirect, url_for, abort

app = Flask(__name__)

IMAGE_DIR = app.static_folder

app.secret_key = "1f805d07d1760cf7d17c332b058cfd"

def init_game():
	images_names = os.listdir(IMAGE_DIR)
	random.shuffle(images_names)
	session["images"] = images_names

def select_from_deck():
	try:
		image_name = session["images"].pop()
	except IndexError:
		image_name = None
	# except KeyError:

	return image_name

@app.route("/")
def index():
	init_game()
	return render_template("index.html")

@app.route("/draw")
def draw():
	if "images" not in session:
		abort(400)
	image_name = select_from_deck()
	if image_name is None:
		return render_template("game_over.html")
	return render_template("showcard.html", image_name=image_name)

if __name__ == "__main__":
	app.run(debug=True)
