# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
from l3.Runtime import _l_
try:
    import hashlib
    _l_(404)

except ImportError:
    pass
with open("your_filename.txt", "rb") as f:
    _l_(408)

    file_hash = hashlib.md5()
    _l_(405)
    while chunk := f.read(8192):
        _l_(407)

        file_hash.update(chunk)
        _l_(406)

print(file_hash.digest())
_l_(409)
print(file_hash.hexdigest())  # to get a printable str instead of bytes
_l_(410)  # to get a printable str instead of bytes

