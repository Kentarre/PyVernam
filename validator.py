import hashlib
import os

class Validator:
    def __init__(self):
        with open(os.path.join(os.getcwd(), 'hash'), "r") as out_file:
            self.hash = out_file.read().replace("\n", "")

    def validate(self, value) -> bool:
        hash_obj = hashlib.sha256(value.encode('utf-8'))
        hex_dig = hash_obj.hexdigest()
        return self.hash == hex_dig