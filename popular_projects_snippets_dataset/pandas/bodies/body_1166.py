# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_multiindex.py
# GH46173
df = DataFrame.from_dict(
    {
        ("foo",): [1, 2, 3],
        ("bar",): [5, 6, 7],
        (None,): [8, 9, 0],
    }
)
with pytest.raises(KeyError, match="missing_key"):
    df[[("missing_key",)]]
