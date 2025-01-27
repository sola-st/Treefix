# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
tuples = [("foo", "car"), ("foo", "bike"), ("bar", "car")]
df.index = MultiIndex.from_tuples(tuples, names=["idx1", "idx2"])
expected_with_index = expected_html(datapath, "index_5")
assert df.to_html() == expected_with_index
assert df.to_html(index=False) == expected_without_index
