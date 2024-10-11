# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# GH 11497

idx = Index([1, 2], dtype="int64", name="idx")
ser = Series([0.1, 0.2], index=idx, name="s")

# loc
with pytest.raises(KeyError, match=r"\[3\] not in index"):
    ser.loc[[3, 2, 3]]

with pytest.raises(KeyError, match=r"not in index"):
    ser.loc[[3, 2, 3, "x"]]

exp_idx = Index([2, 2, 1], dtype="int64", name="idx")
expected = Series([0.2, 0.2, 0.1], index=exp_idx, name="s")
result = ser.loc[[2, 2, 1]]
tm.assert_series_equal(result, expected, check_index_type=True)

with pytest.raises(KeyError, match=r"\['x'\] not in index"):
    ser.loc[[2, 2, "x", 1]]

# raises as nothing is in the index
msg = (
    rf"\"None of \[NumericIndex\(\[3, 3, 3\], dtype='{np.int_().dtype}', "
    r"name='idx'\)\] are in the \[index\]\""
)
with pytest.raises(KeyError, match=msg):
    ser.loc[[3, 3, 3]]

with pytest.raises(KeyError, match="not in index"):
    ser.loc[[2, 2, 3]]

idx = Index([1, 2, 3], dtype="int64", name="idx")
with pytest.raises(KeyError, match="not in index"):
    Series([0.1, 0.2, 0.3], index=idx, name="s").loc[[3, 4, 4]]

idx = Index([1, 2, 3, 4], dtype="int64", name="idx")
with pytest.raises(KeyError, match="not in index"):
    Series([0.1, 0.2, 0.3, 0.4], index=idx, name="s").loc[[5, 3, 3]]

idx = Index([1, 2, 3, 4], dtype="int64", name="idx")
with pytest.raises(KeyError, match="not in index"):
    Series([0.1, 0.2, 0.3, 0.4], index=idx, name="s").loc[[5, 4, 4]]

idx = Index([4, 5, 6, 7], dtype="int64", name="idx")
with pytest.raises(KeyError, match="not in index"):
    Series([0.1, 0.2, 0.3, 0.4], index=idx, name="s").loc[[7, 2, 2]]

idx = Index([1, 2, 3, 4], dtype="int64", name="idx")
with pytest.raises(KeyError, match="not in index"):
    Series([0.1, 0.2, 0.3, 0.4], index=idx, name="s").loc[[4, 5, 5]]

# iloc
exp_idx = Index([2, 2, 1, 1], dtype="int64", name="idx")
expected = Series([0.2, 0.2, 0.1, 0.1], index=exp_idx, name="s")
result = ser.iloc[[1, 1, 0, 0]]
tm.assert_series_equal(result, expected, check_index_type=True)
