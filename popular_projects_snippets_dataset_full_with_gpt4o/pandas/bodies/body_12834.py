# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_readlines.py
# GH 35849
# Test ValueError when orient is not 'records'
df = DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
msg = (
    r"mode='a' \(append\) is only supported when"
    "lines is True and orient is 'records'"
)
with pytest.raises(ValueError, match=msg):
    df.to_json(mode="a", orient=orient_)
