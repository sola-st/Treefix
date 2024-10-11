# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#20991
idx = Index(
    [(1,), (1, 2)],
    name="A",
    tupleize_cols=False,
)
df = DataFrame(index=idx)

result = df.loc[[tpl]]
idx = Index([tpl], name="A", tupleize_cols=False)
expected = DataFrame(index=idx)
tm.assert_frame_equal(result, expected)
