# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH 13653
s = Series(["", "Hello", "World", "", "", "Mooooo", "", ""])
res = s.to_string(index=False)
exp = "      \n Hello\n World\n      \n      \nMooooo\n      \n      "
assert re.match(exp, res)
