from google.cloud import storage

class Google_Storage:

    def __init__(self, bucket_name):
        self.storage_client = storage.Client.from_service_account_json('credentials-storage-admin.json')
        self.bucket_name = bucket_name

    def create_bucket(self):
        
        """Creates a new bucket."""
        bucket = self.storage_client.create_bucket(self.bucket_name)
        print('Bucket {} created'.format(bucket.name))

    def delete_bucket(self):

        """Deletes a bucket. The bucket must be empty."""
        bucket = self.storage_client.get_bucket(self.bucket_name)
        bucket.delete()
        print('Bucket {} deleted'.format(bucket.name))

    def list_buckets(self):
        
        """List Buckets."""
        return self.storage_client.list_buckets()

    def list_blobs(self):
        """Lists all the blobs in the bucket."""
        bucket = self.storage_client.get_bucket(self.bucket_name)

        return bucket.list_blobs()

    def upload_file(self, file_stream, filename, content_type):
        """
        Uploads a file to a given Cloud Storage bucket and returns the public url
        to the new object.
        """
        filename = self.clean_filename(filename)

        client = self.storage_client
        bucket = client.bucket(self.bucket_name)
        blob = bucket.blob(filename)

        blob.upload_from_string(
            file_stream,
            content_type=content_type)
        
        blob.make_public()

        url = blob.public_url

        import six
        if isinstance(url, six.binary_type):
            url = url.decode('utf-8')

        return url

    def clean_filename(self, filename):
        import unicodedata
        import string

        whitelist = "-_.() %s%s" % (string.ascii_letters, string.digits)
        # replace spaces
        filename = filename.replace(" ",'_')
        
        # keep only valid ascii chars
        cleaned_filename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore').decode()
        
        # keep only whitelisted chars
        return ''.join(c for c in cleaned_filename if c in whitelist)