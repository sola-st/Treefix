# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# nothing to merge
target, source = target_source
merged = target.join(source.reindex([]), on="C")
for col in source:
    assert col in merged
    assert merged[col].isna().all()

merged2 = target.join(source.reindex([]), on="C", how="inner")
tm.assert_index_equal(merged2.columns, merged.columns)
assert len(merged2) == 0
