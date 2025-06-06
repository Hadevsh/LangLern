from flask import Blueprint, render_template
import argostranslate.package
import argostranslate.translate

main = Blueprint('main', __name__)

# Utils
def translate(text, from_code, to_code):
    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
    translated_text = argostranslate.translate.translate(text, from_code, to_code)

    return translated_text

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

@main.route("/about")
def about():
    return render_template("about.html")