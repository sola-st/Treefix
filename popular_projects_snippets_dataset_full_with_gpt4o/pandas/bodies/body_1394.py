# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 25567
obj = gen_obj(frame_or_series, index)
idxr = indexer_sli(obj)
nd3 = np.random.randint(5, size=(2, 2, 2))

if indexer_sli is tm.iloc:
    err = ValueError
    msg = f"Cannot set values with ndim > {obj.ndim}"
else:
    err = ValueError
    msg = "|".join(
        [
            r"Buffer has wrong number of dimensions \(expected 1, got 3\)",
            "Cannot set values with ndim > 1",
            "Index data must be 1-dimensional",
            "Data must be 1-dimensional",
            "Array conditional must be same shape as self",
        ]
    )

with pytest.raises(err, match=msg):
    idxr[nd3] = 0
