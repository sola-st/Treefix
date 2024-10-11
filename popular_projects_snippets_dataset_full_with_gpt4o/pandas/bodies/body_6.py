# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 26513
df = DataFrame({"A": [0, 1], "B": [1, 2]})
msg = "Must provide"

with pytest.raises(TypeError, match=msg):
    df.agg()
