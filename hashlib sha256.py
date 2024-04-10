import hashlib
text = input()
text_hash = text.encode()
text_hash = hashlib.sha256(text_hash)
print(text_hash.hexdigest())
