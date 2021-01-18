import os
import pickle
from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
import numpy as np
from src import utils
from src.routes.process import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = utils.path_from_root('uploads')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}


def convert(o):
    if isinstance(o, np.int64) or isinstance(o, np.int32): return int(o)
    raise TypeError


from collections import Sequence


def recursive_map(seq, func):
    for item in seq:
        if isinstance(item, Sequence):
            yield type(item)(recursive_map(item, func))
        else:
            yield func(item)


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
        # ocr_res = ocr(filepath)
        ocr_res = pickle.load(open(utils.path_from_root('dump/ocr_res'), "rb"))
        os.remove(filepath)
        return jsonify(format_response(ocr_res))


if __name__ == '__main__':
    app.run()
