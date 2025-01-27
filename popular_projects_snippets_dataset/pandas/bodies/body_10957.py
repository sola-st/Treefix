# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_value_counts.py
# Test for result column label duplicating an input column label
gb = DataFrame([[1, 2, 3]], columns=["a", "b", expected_label]).groupby(
    "a", as_index=False
)
msg = f"Column label '{expected_label}' is duplicate of result column"
with pytest.raises(ValueError, match=msg):
    gb.value_counts(normalize=normalize)
