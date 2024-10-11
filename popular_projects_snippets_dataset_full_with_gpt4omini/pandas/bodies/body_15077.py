# Extracted from ./data/repos/pandas/pandas/tests/base/test_misc.py
# numpy.searchsorted calls obj.searchsorted under the hood.
# See gh-12238
obj = index_or_series_obj

if isinstance(obj, pd.MultiIndex):
    # See gh-14833
    request.node.add_marker(
        pytest.mark.xfail(
            reason="np.searchsorted doesn't work on pd.MultiIndex: GH 14833"
        )
    )
elif obj.dtype.kind == "c" and isinstance(obj, Index):
    # TODO: Should Series cases also raise? Looks like they use numpy
    #  comparison semantics https://github.com/numpy/numpy/issues/15981
    mark = pytest.mark.xfail(reason="complex objects are not comparable")
    request.node.add_marker(mark)

max_obj = max(obj, default=0)
index = np.searchsorted(obj, max_obj)
assert 0 <= index <= len(obj)

index = np.searchsorted(obj, max_obj, sorter=range(len(obj)))
assert 0 <= index <= len(obj)
