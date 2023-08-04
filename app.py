from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def gallery():
    image_files = os.listdir("static/images")  # Assuming your images are in the static/images directory
    return render_template("gallery.html", image_files=image_files)

if __name__ == "__main__":
    app.run(debug=True)