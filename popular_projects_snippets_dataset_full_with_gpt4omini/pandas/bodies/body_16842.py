# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
NA_SENTINEL = -1234567  # drop_duplicates not so NA-friendly...

jvalues = join_chunk.fillna(NA_SENTINEL).drop_duplicates().values
svalues = source.fillna(NA_SENTINEL).drop_duplicates().values

rows = {tuple(row) for row in jvalues}
assert len(rows) == len(source)
assert all(tuple(row) in rows for row in svalues)
