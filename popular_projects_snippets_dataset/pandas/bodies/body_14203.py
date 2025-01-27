# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
for f in (str, repr, methodcaller("isoformat")):
    assert f(NaT) == "NaT"
