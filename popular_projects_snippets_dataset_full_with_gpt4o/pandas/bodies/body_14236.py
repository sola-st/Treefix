# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df = DataFrame([list("abcd"), list("efgh")], columns=columns)
result = df.to_html(justify=justify)
expected = expected_html(datapath, expected)
assert result == expected
