import os
import random
import string

from flask import Flask, request, abort
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['STATIC_FOLDER'] = f"{os.getenv('APP_FOLDER')}/static/uploads"


def _create_random_file_name():
    letters = string.ascii_letters + string.digits
    # used to set the length of the generated filenames, can be increased for more values
    # with a length of 5 there are 56800235584 Random File names possible (52 letters + 10 numbers^6)
    random_file_name_length = 6
    return ''.join(random.choice(letters) for i in range(random_file_name_length))


@app.route('/upload', methods=['POST'])
def sharex_upload():
    # checks if the parameter "key" is set and also matches the key in the env config
    if request.args.get('key') != os.getenv('UPLOAD_KEY'):
        return abort(404)
    if 'image' not in request.files:
        return abort(404)
    static_path = app.config['STATIC_FOLDER']
    random_file_name = _create_random_file_name()
    # could lead to an infinite loop if all combinations ares exhausted (very unlikely) (ignored for now)
    while os.path.isfile(os.path.join(static_path, random_file_name)):
        random_file_name = _create_random_file_name()

    upload = request.files['image']
    file_name = secure_filename(random_file_name)
    upload.save(os.path.join(static_path, file_name))
    print(upload)
    return request.host_url + str(file_name)


if __name__ == '__main__':
    app.run()
