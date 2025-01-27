# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
# GH 36702. Raise when trying to add list of array-like to DataFrame
df = DataFrame({"x": [1, 2], "y": [1, 2]})

msg = f"Unable to coerce list of {type(to_add[0])} to Series/DataFrame"
with pytest.raises(ValueError, match=msg):
    df + to_add
with pytest.raises(ValueError, match=msg):
    to_add + df
