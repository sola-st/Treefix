# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# gh-27991

# default setting no truncation even if above min_rows
df = DataFrame({"a": range(20)})
result = df._repr_html_()
expected = expected_html(datapath, "html_repr_min_rows_default_no_truncation")
assert result == expected

# default of max_rows 60 triggers truncation if above
df = DataFrame({"a": range(61)})
result = df._repr_html_()
expected = expected_html(datapath, "html_repr_min_rows_default_truncated")
assert result == expected
