# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
df = DataFrame(index=arrays, columns=arrays)
result = df.to_html(max_rows=7, max_cols=7, sparsify=sparsify)
expected = expected_html(datapath, expected)
assert result == expected
