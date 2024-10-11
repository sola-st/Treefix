# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
df.index = Index(["foo", "bar", "baz"], name="idx")
expected_with_index = expected_html(datapath, "index_3")
assert df.to_html() == expected_with_index
assert df.to_html(index=False) == expected_without_index
