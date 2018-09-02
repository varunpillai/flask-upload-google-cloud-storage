import os
from flask import Flask, request
from GoogleStorage import Google_Storage
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        file.filename = secure_filename(file.filename)
        google_storage = Google_Storage('movti-interview')

        public_url = google_storage.upload_file(
            file.read(),
            file.filename,
            file.content_type
        )
        return 'Public URL:' + public_url
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''