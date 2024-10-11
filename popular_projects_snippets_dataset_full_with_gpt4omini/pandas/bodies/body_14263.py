# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# gh-27991

df = DataFrame({"a": range(61)})
expected = expected_html(datapath, expected)
with option_context("display.max_rows", max_rows, "display.min_rows", min_rows):
    result = df._repr_html_()
assert result == expected
