# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
df = DataFrame({"a": range(20)})

# default setting no truncation even if above min_rows
assert ".." not in repr(df)
assert ".." not in df._repr_html_()

df = DataFrame({"a": range(61)})

# default of max_rows 60 triggers truncation if above
assert ".." in repr(df)
assert ".." in df._repr_html_()

with option_context("display.max_rows", 10, "display.min_rows", 4):
    # truncated after first two rows
    assert ".." in repr(df)
    assert "2  " not in repr(df)
    assert "..." in df._repr_html_()
    assert "<td>2</td>" not in df._repr_html_()

with option_context("display.max_rows", 12, "display.min_rows", None):
    # when set to None, follow value of max_rows
    assert "5    5" in repr(df)
    assert "<td>5</td>" in df._repr_html_()

with option_context("display.max_rows", 10, "display.min_rows", 12):
    # when set value higher as max_rows, use the minimum
    assert "5    5" not in repr(df)
    assert "<td>5</td>" not in df._repr_html_()

with option_context("display.max_rows", None, "display.min_rows", 12):
    # max_rows of None -> never truncate
    assert ".." not in repr(df)
    assert ".." not in df._repr_html_()
