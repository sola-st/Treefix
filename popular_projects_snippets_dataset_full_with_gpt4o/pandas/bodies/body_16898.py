# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
# see gh-7751
values = [0, 0, 0, 0, 1, 2, 3]

if msg is not None:
    with pytest.raises(ValueError, match=msg):
        qcut(values, 3, **kwargs)
else:
    result = qcut(values, 3, **kwargs)
    expected = IntervalIndex([Interval(-0.001, 1), Interval(1, 3)])
    tm.assert_index_equal(result.categories, expected)
