# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py

# single axis
idx = list("ABCD")

for axis in frame_or_series._AXIS_ORDERS:
    kwargs = {axis: idx}
    obj = construct(frame_or_series, 4, **kwargs)

    # rename a single axis
    result = obj.rename(**{axis: func})
    expected = obj.copy()
    setattr(expected, axis, list("abcd"))
    tm.assert_equal(result, expected)
