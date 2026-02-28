from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

anime_db = [
    {
        "id": 1,
        "title": "Naruto Shippuden Hindi",
        "poster": "https://i.imgur.com/7glcxNc.jpeg",
        "episodes": []
    },
    {
        "id": 2,
        "title": "One Piece Hindi",
        "poster": "https://image.tmdb.org/t/p/w500/6WDumtqabD8G9bLo8fLB6Bzxr6N.jpg",
        "episodes": []
    }
]

@app.route('/')
def home():
    return render_template("index.html", animes=anime_db)

@app.route('/admin')
def admin():
    return render_template("admin.html", animes=anime_db)

@app.route('/upload', methods=['POST'])
def upload():
    anime_id = int(request.form['anime_id'])
    video = request.files['video']

    if video:
        filename = secure_filename(video.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video.save(save_path)

        for anime in anime_db:
            if anime["id"] == anime_id:
                anime["episodes"].append("/static/uploads/" + filename)

    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
