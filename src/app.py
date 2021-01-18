import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from src import utils
from src.routes.process import ocr

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = utils.path_from_root('/uploads')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}


@app.route('/process', methods=['POST'])
def process():
    # check if the post request has the file part
    if 'image' not in request.files:
        flash('No image')
        return redirect(request.url)
    image = request.files['image']
    if image.filename == '':
        flash('No selected image')
        return redirect(request.url)
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return ocr(image)


if __name__ == '__main__':
    app.run()
