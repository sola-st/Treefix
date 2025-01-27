# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
expected = expected_html(datapath, expected)
result = df.to_html(formatters=formatters)
assert result == expected
