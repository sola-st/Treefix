# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_series_equal.py
kwargs = {"check_index_type": check_index_type}

if check_index_type:
    with pytest.raises(AssertionError, match=msg):
        tm.assert_series_equal(s1, s2, **kwargs)
else:
    tm.assert_series_equal(s1, s2, **kwargs)
