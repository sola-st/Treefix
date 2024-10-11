# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#48296 - at shouldn't modify multiple columns
df = DataFrame({"a": [1, 2], "b": [3, 4]})
new_row = [6, 7]
with pytest.raises(
    InvalidIndexError,
    match=f"You can only assign a scalar value not a \\{type(new_row)}",
):
    df.at[5] = new_row
