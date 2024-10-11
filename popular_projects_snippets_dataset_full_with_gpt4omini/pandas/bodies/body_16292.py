# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH15125
# test dtype parameter has no side effects on copy=True
for data in [[1.0], np.array([1.0])]:
    x = Series(data)
    y = Series(x, copy=True, dtype=float)

    # copy=True maintains original data in Series
    tm.assert_series_equal(x, y)

    # changes to origin of copy does not affect the copy
    x[0] = 2.0
    assert not x.equals(y)
    assert x[0] == 2.0
    assert y[0] == 1.0
