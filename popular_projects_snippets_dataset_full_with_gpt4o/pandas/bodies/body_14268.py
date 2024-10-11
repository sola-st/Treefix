# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_printing.py
letters = string.ascii_letters
try:
    raw = bytes(letters, encoding=cf.get_option("display.encoding"))
except TypeError:
    raw = bytes(letters)
b = str(raw.decode("utf-8"))
res = printing.pprint_thing(b, quote_strings=True)
assert res == repr(b)
res = printing.pprint_thing(b, quote_strings=False)
assert res == b
