# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4706499/how-do-i-append-to-a-file
from l3.Runtime import _l_
with open("foo", "a") as f:
    _l_(12518)

    f.write("cool beans...")
    _l_(12517)

