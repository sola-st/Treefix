# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_html.py
# GH 22579
df = DataFrame(
    {"a": range(10), "b": range(10, 20), "c": range(10, 20), "d": range(10, 20)}
)
df.columns = MultiIndex.from_product([["a", "b"], ["c", "d"]])
df.index = MultiIndex.from_product([["a", "b"], ["c", "d", "e", "f", "g"]])
result = df.to_html(index=False)
expected = expected_html(datapath, "gh22579_expected_output")
assert result == expected
