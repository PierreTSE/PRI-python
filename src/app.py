import os

from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename

from src import utils
from src.routes.process import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = utils.path_from_root('uploads')
app.config["DEBUG"] = False


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
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)
        ocr_res = ocr(filepath)
        os.remove(filepath)
        return jsonify(format_response(ocr_res))


if __name__ == '__main__':
    app.run()
