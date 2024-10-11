# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#24255
# case where `addend = periods * stride` overflows int64 bounds
#  but not uint64 bounds
dti = date_range(start="1677-09-22", end="2262-04-11", freq="D")

dti2 = date_range(start=dti[0], periods=len(dti), freq="D")
assert dti2.equals(dti)

dti3 = date_range(end=dti[-1], periods=len(dti), freq="D")
assert dti3.equals(dti)
