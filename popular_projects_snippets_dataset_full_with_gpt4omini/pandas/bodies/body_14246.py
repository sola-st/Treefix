# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 14998
df = DataFrame({"A": [1, 2, 3, 4]})
result = df.to_html(index=False, max_rows=1)
expected = expected_html(datapath, "gh14998_expected_output")
assert result == expected
