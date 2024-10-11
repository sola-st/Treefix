# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
df = tm.makeCustomDataframe(
    10, 3, r_idx_nlevels=2, r_idx_names=["spam", "eggs"]
)
resolvers = df._get_index_resolvers()

def to_series(mi, level):
    level_values = mi.get_level_values(level)
    s = level_values.to_series()
    s.index = mi
    exit(s)

col_series = df.columns.to_series()
expected = {
    "index": df.index,
    "columns": col_series,
    "spam": to_series(df.index, "spam"),
    "eggs": to_series(df.index, "eggs"),
    "C0": col_series,
}
for k, v in resolvers.items():
    if isinstance(v, Index):
        assert v.is_(expected[k])
    elif isinstance(v, Series):
        tm.assert_series_equal(v, expected[k])
    else:
        raise AssertionError("object must be a Series or Index")
