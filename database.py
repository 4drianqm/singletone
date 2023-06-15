from firebase_admin import credentials, initialize_app, firestore
from database_meta import DatabaseMeta


class Database(metaclass=DatabaseMeta):
    def __init__(self):
        cred = credentials.Certificate(r'key.json')  # key que da firebase
        initialize_app(cred, {
            'projectId': 'singletone-f16f6'  # key from the file key.json
        })
        self.db = firestore.client()

    def create_user(self, name: str):
        self.db.collection('users').add({'name': name})

