# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
from l3.Runtime import _l_
try:
    _l_(12652)

    os.remove(filename)
    _l_(12649)
except FileNotFoundError:
    _l_(12651)

    pass
    _l_(12650)

