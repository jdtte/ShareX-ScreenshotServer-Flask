import os
import random
import string

from flask import Flask, request, abort
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5000 * 1024 * 1024  # 5 GB max size Note this will require a server with more then 5 gb of memory
app.config['STATIC_FOLDER'] = f"{os.getenv('APP_FOLDER')}/{UPLOAD_FOLDER}"


def _create_random_file_name():
    letters = string.ascii_letters + string.digits
    # used to set the length of the generated filenames, can be increased for more values
    # with a length of 5 there are 56800235584 Random File names possible (52 letters + 10 numbers^6)
    random_file_name_length = 6
    return ''.join(random.choice(letters) for i in range(random_file_name_length))


def _check_if_file_exists_ignoring_fileending(filename):
    with os.scandir(UPLOAD_FOLDER) as file_dir:
        for entry in file_dir:
            if entry.name.startswith(filename) and entry.is_file():
                return True
    return False


@app.route('/upload', methods=['POST'])
def sharex_upload():
    # checks if the parameter "key" is set and also matches the key in the env config
    if request.args.get('key') != os.getenv('UPLOAD_KEY'):
        return abort(404)
    if 'image' not in request.files:
        return abort(404)

    random_file_name = _create_random_file_name()
    # could lead to an infinite loop if all combinations ares exhausted (very unlikely) (ignored for now)
    while _check_if_file_exists_ignoring_fileending(random_file_name):
        random_file_name = _create_random_file_name()

    upload = request.files['image']

    file_ending = os.path.splitext(upload.filename)[-1]
    file_name = secure_filename(random_file_name + file_ending)
    upload.save(os.path.join(app.config['STATIC_FOLDER'], file_name))
    print(upload)
    return request.host_url + str(file_name)


if __name__ == '__main__':
    app.run()
