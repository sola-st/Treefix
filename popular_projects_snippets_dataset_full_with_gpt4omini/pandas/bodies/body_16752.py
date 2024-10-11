# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# issue: 24782
a = DataFrame({col1: [1, 2, 3]})
b = DataFrame({col2: [3, 4, 5]})

# TODO: might reconsider current raise behaviour, see issue 24782
msg = "columns overlap but no suffix specified"
with pytest.raises(ValueError, match=msg):
    merge(a, b, left_index=True, right_index=True, suffixes=suffixes)
