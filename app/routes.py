from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route('/flashcards')
def flashcards():
    sample_flashcards = [
        {'front': 'Hallo', 'back': 'Hello'},
        {'front': 'Dank je', 'back': 'Thank you'},
        {'front': 'Tot ziens', 'back': 'Goodbye'}
    ]
    return render_template('flashcards.html', flashcards=sample_flashcards)
