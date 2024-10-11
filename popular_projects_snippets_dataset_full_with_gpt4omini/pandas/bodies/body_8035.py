# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
if cast_as_obj:
    result = Index(index.astype(object))
else:
    result = Index(index)

tm.assert_index_equal(result, index)

if isinstance(index, DatetimeIndex):
    assert result.tz == index.tz
    if cast_as_obj:
        # GH#23524 check that Index(dti, dtype=object) does not
        #  incorrectly raise ValueError, and that nanoseconds are not
        #  dropped
        index += pd.Timedelta(nanoseconds=50)
        result = Index(index, dtype=object)
        assert result.dtype == np.object_
        assert list(result) == list(index)
