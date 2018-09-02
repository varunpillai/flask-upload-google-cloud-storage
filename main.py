import os
from flask import Flask, request, render_template
from GoogleStorage import Google_Storage
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.run(debug=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    google_storage = Google_Storage('movti-interview')
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

        public_url = google_storage.upload_file(
            file.read(),
            file.filename,
            file.content_type
        )
        return render_template('upload_file.html', files=google_storage.list_blobs(), public_url=public_url)
    return render_template('upload_file.html', files=google_storage.list_blobs())

@app.route('/delete_file/<file_name>')
def delete_file(file_name):
    google_storage = Google_Storage('movti-interview')
    google_storage.delete_blob(file_name)
    return render_template('upload_file.html', files=google_storage.list_blobs(), file_deleted_name=file_name)