# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#10699
vec = DatetimeIndex(
    [
        Timestamp("2000-01-05 00:15:00"),
        Timestamp("2000-01-31 00:23:00"),
        Timestamp("2000-01-01"),
        Timestamp("2000-03-31"),
        Timestamp("2000-02-29"),
        Timestamp("2000-12-31"),
        Timestamp("2000-05-15"),
        Timestamp("2001-06-15"),
    ]
)
vec = tm.box_expected(vec, box_with_array)
vec_items = vec.iloc[0] if box_with_array is pd.DataFrame else vec

# DateOffset relativedelta fastpath
relative_kwargs = [
    ("years", 2),
    ("months", 5),
    ("days", 3),
    ("hours", 5),
    ("minutes", 10),
    ("seconds", 2),
    ("microseconds", 5),
]
for i, (unit, value) in enumerate(relative_kwargs):
    off = DateOffset(**{unit: value})

    expected = DatetimeIndex([x + off for x in vec_items])
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(expected, vec + off)

    expected = DatetimeIndex([x - off for x in vec_items])
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(expected, vec - off)

    off = DateOffset(**dict(relative_kwargs[: i + 1]))

    expected = DatetimeIndex([x + off for x in vec_items])
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(expected, vec + off)

    expected = DatetimeIndex([x - off for x in vec_items])
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(expected, vec - off)
    msg = "(bad|unsupported) operand type for unary"
    with pytest.raises(TypeError, match=msg):
        off - vec
