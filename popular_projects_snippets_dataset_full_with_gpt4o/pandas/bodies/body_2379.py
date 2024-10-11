# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_insert.py
# GH#42403
df = DataFrame({"col1": [1, 2], "col2": [3, 4]})

msg = r"Expected a 1D array, got an array with shape \(2, 2\)"
with pytest.raises(ValueError, match=msg):
    df.insert(1, "newcol", df)
