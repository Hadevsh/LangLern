from flask import Blueprint, render_template, request, jsonify
import argostranslate.package
import argostranslate.translate

main = Blueprint('main', __name__)

# Utils
def translate(text, from_code, to_code):
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    pkg = next(
        p for p in available_packages
        if p.from_code == from_code and p.to_code == to_code
    )
    argostranslate.package.install_from_path(pkg.download())
    return argostranslate.translate.translate(text, from_code, to_code)

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

# Translation route
@main.route("/translate", methods=["POST"])
def do_translate():
    data = request.get_json()
    word = data.get("word", "")
    src = data.get("from_code", "en") # default English
    tgt = data.get("to_code", "nl") # default Dutch

    if not word:
        return jsonify({"error": "No word provided"}), 400

    try:
        result = translate(word, src, tgt)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"translation": result})