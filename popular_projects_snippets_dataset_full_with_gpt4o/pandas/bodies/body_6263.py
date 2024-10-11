# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
arr = data.copy()

# TODO(xfail) this raises KeyError about labels not found (it tries label-based)
# for list of labels with Series
if box_in_series:
    arr = pd.Series(data, index=[tm.rands(4) for _ in range(len(data))])

msg = "Cannot index with an integer indexer containing NA values"
with pytest.raises(ValueError, match=msg):
    arr[idx] = arr[0]
