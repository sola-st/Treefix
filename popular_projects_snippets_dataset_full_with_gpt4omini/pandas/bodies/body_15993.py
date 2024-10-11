# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename.py
# GH 46889
ser = Series(["foo", "bar"])
match = re.escape("[2] not found in axis")
with pytest.raises(KeyError, match=match):
    ser.rename({2: 9}, errors="raise")
