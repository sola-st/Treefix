# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_sort.py
# GH#41518
df = DataFrame({1: [1, 2], "a": [3, 4]})
msg = "The 'sort' keyword only accepts boolean values; None was passed."
with pytest.raises(ValueError, match=msg):
    pd.concat([df, df], sort=None)
