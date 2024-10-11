# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 25567
obj = gen_obj(frame_or_series, index)
idxr = indexer_sli(obj)
nd3 = np.random.randint(5, size=(2, 2, 2))

msgs = []
if frame_or_series is Series and indexer_sli in [tm.setitem, tm.iloc]:
    msgs.append(r"Wrong number of dimensions. values.ndim > ndim \[3 > 1\]")
    if using_array_manager:
        msgs.append("Passed array should be 1-dimensional")
if frame_or_series is Series or indexer_sli is tm.iloc:
    msgs.append(r"Buffer has wrong number of dimensions \(expected 1, got 3\)")
    if using_array_manager:
        msgs.append("indexer should be 1-dimensional")
if indexer_sli is tm.loc or (
    frame_or_series is Series and indexer_sli is tm.setitem
):
    msgs.append("Cannot index with multidimensional key")
if frame_or_series is DataFrame and indexer_sli is tm.setitem:
    msgs.append("Index data must be 1-dimensional")
if isinstance(index, pd.IntervalIndex) and indexer_sli is tm.iloc:
    msgs.append("Index data must be 1-dimensional")
if isinstance(index, (pd.TimedeltaIndex, pd.DatetimeIndex, pd.PeriodIndex)):
    msgs.append("Data must be 1-dimensional")
if len(index) == 0 or isinstance(index, pd.MultiIndex):
    msgs.append("positional indexers are out-of-bounds")
if type(index) is Index and not isinstance(index._values, np.ndarray):
    # e.g. Int64
    msgs.append("values must be a 1D array")

    # string[pyarrow]
    msgs.append("only handle 1-dimensional arrays")

msg = "|".join(msgs)

potential_errors = (IndexError, ValueError, NotImplementedError)
with pytest.raises(potential_errors, match=msg):
    idxr[nd3]
