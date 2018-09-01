from GoogleStorage import Google_Storage
import codecs
import mimetypes

def upload_image_file(file):
    """
    Upload the user-uploaded file to Google Cloud Storage and retrieve its
    publicly-accessible URL.
    """
    if not file:
        return None

    google_storage = Google_Storage()

    public_url = google_storage.upload_file(
        file.read(),
        file.name,
        mimetypes.MimeTypes().guess_type(file.name)[0]
    )

    return public_url

with codecs.open('balao.jpeg', "r",encoding='utf-8', errors='ignore') as f:
    print(upload_image_file(f))