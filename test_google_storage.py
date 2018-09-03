from GoogleStorage import Google_Storage
class TestGoogleStorage(object):

    def test_bucket_creation(self):
        bucket_name = 'bucket-teste-pytest1'
        google_storage = Google_Storage(bucket_name)
        google_storage.create_bucket()
        assert bucket_name in google_storage.list_buckets_names()
        google_storage.delete_bucket()

    def test_bucket_list(self):
        bucket_name = 'bucket-teste-pytest1'
        google_storage = Google_Storage(bucket_name)
        google_storage.create_bucket()
        assert bucket_name in google_storage.list_buckets_names()
        assert 'bucket-example' not in google_storage.list_buckets_names()
        google_storage.delete_bucket()