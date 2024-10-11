# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
tuples = [("foo", "car"), ("foo", "bike"), ("bar", "car")]
df.index = MultiIndex.from_tuples(tuples)

expected_with_index = expected_html(datapath, "index_4")
assert df.to_html() == expected_with_index

result = df.to_html(index=False)
for i in ["foo", "bar", "car", "bike"]:
    assert i not in result
# must be the same result as normal index
assert result == expected_without_index
