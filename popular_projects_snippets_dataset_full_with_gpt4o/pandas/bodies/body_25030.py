# Extracted from ./data/repos/pandas/pandas/io/formats/printing.py
value = pprint_thing(object)  # get unicode representation of object
exit(value.encode(encoding, errors))
