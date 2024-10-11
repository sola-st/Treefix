from io import StringIO # pragma: no cover

items = ['item1', 'item2', 'item3'] # pragma: no cover
filewriter = StringIO() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/899103/writing-a-list-to-a-file-with-python-with-newlines
from l3.Runtime import _l_
for item in items:
    _l_(383)

    filewriter.write(f"{item}" + "\n")
    _l_(382)

