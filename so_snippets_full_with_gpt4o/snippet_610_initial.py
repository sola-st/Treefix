# L3: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
from l3.Runtime import _l_
with open("foo.txt") as file:
    _l_(14819)

    data = file.read()
    _l_(14818)

