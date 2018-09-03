# Upload file to google cloud storage

### Software requirements
* Virtualenv: Versão >= 16.0.0
* Pip3: Versão >= 10.0.1

### Configuration

* You need have a key from a google cloud storage service with access "Storage Admin"
* The file needs have the name: "credentials-storage-admin.json"

### Installation
```bash
$ virtualenv interview-env
$ source interview-env/bin/activate
$ pip3 install -r requirements.txt
```

### Execution
```bash
$ source interview-env/bin/activate
$ export FLASK_ENV=development
$ flask run
```

### Run Tests
```bash
$ source interview-env/bin/activate
$ pytest
```