# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
dti = date_range("2016-01-01", periods=3)
pi = dti.to_period("D")

other = non_comparable_idx

msg = re.escape(f"Cannot compare dtypes {pi.dtype} and {other.dtype}")
with pytest.raises(TypeError, match=msg):
    pi.get_indexer(other, method=method)

for dtype in ["object", "category"]:
    other2 = other.astype(dtype)
    if dtype == "object" and isinstance(other, PeriodIndex):
        continue
    # Two different error message patterns depending on dtypes
    msg = "|".join(
        [
            re.escape(msg)
            for msg in (
                f"Cannot compare dtypes {pi.dtype} and {other.dtype}",
                " not supported between instances of ",
            )
        ]
    )
    with pytest.raises(TypeError, match=msg):
        pi.get_indexer(other2, method=method)
