# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
# GH#49340 all NaT/None/nan and at least 1 NaT -> datetime64[ns],
#  matching Series behavior
values = [NaT, val]

idx = Index(values)
assert idx.dtype == "datetime64[ns]" and idx.isna().all()

idx = Index(values[::-1])
assert idx.dtype == "datetime64[ns]" and idx.isna().all()

idx = Index(np.array(values, dtype=object))
assert idx.dtype == "datetime64[ns]" and idx.isna().all()

idx = Index(np.array(values, dtype=object)[::-1])
assert idx.dtype == "datetime64[ns]" and idx.isna().all()
