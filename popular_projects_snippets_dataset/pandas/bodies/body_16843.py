# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
for c in source_columns:
    if c in join_col:
        continue
    assert join_chunk[c].isna().all()
