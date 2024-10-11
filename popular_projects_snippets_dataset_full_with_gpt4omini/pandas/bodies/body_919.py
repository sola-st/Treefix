# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_at.py
# GH#48729 .at should raise InvalidIndexError when assigning rows
df = DataFrame(index=["a"], columns=["col1", "col2"])
new_row = [123, 15]
with pytest.raises(
    InvalidIndexError,
    match=f"You can only assign a scalar value not a \\{type(new_row)}",
):
    df.at["a"] = new_row
