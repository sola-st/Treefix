# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py

# 11594, 12045
# when truncated the dtypes of the splits can differ

# 11594
s = Series(
    [datetime(2012, 1, 1)] * 10
    + [datetime(1012, 1, 2)]
    + [datetime(2012, 1, 3)] * 10
)

with option_context("display.max_rows", 8):
    result = str(s)
    assert "object" in result

# 12045
df = DataFrame({"text": ["some words"] + [None] * 9})

with option_context("display.max_rows", 8, "display.max_columns", 3):
    result = str(df)
    assert "None" in result
    assert "NaN" not in result
