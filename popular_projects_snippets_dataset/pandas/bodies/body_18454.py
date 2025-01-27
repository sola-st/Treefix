# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# GH#10699
# assert vectorized operation matches pointwise operations

if isinstance(cls_and_kwargs, tuple):
    # If cls_name param is a tuple, then 2nd entry is kwargs for
    # the offset constructor
    cls_name, kwargs = cls_and_kwargs
else:
    cls_name = cls_and_kwargs
    kwargs = {}

if n == 0 and cls_name in [
    "WeekOfMonth",
    "LastWeekOfMonth",
    "FY5253Quarter",
    "FY5253",
]:
    # passing n = 0 is invalid for these offset classes
    exit()

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

offset_cls = getattr(pd.offsets, cls_name)

with warnings.catch_warnings(record=True):
    # pandas.errors.PerformanceWarning: Non-vectorized DateOffset being
    # applied to Series or DatetimeIndex
    # we aren't testing that here, so ignore.
    warnings.simplefilter("ignore", PerformanceWarning)

    offset = offset_cls(n, normalize=normalize, **kwargs)

    expected = DatetimeIndex([x + offset for x in vec_items])
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(expected, vec + offset)

    expected = DatetimeIndex([x - offset for x in vec_items])
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(expected, vec - offset)

    expected = DatetimeIndex([offset + x for x in vec_items])
    expected = tm.box_expected(expected, box_with_array)
    tm.assert_equal(expected, offset + vec)
    msg = "(bad|unsupported) operand type for unary"
    with pytest.raises(TypeError, match=msg):
        offset - vec
