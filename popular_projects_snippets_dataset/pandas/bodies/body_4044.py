# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
"""
    Check that operator opname works as advertised on frame

    Parameters
    ----------
    opname : str
        Name of the operator to test on frame
    alternative : function
        Function that opname is tested against; i.e. "frame.opname()" should
        equal "alternative(frame)".
    frame : DataFrame
        The object that the tests are executed on
    has_skipna : bool, default True
        Whether the method "opname" has the kwarg "skip_na"
    check_dtype : bool, default True
        Whether the dtypes of the result of "frame.opname()" and
        "alternative(frame)" should be checked.
    check_dates : bool, default false
        Whether opname should be tested on a Datetime Series
    rtol : float, default 1e-5
        Relative tolerance.
    atol : float, default 1e-8
        Absolute tolerance.
    skipna_alternative : function, default None
        NaN-safe version of alternative
    """
f = getattr(frame, opname)

if check_dates:
    df = DataFrame({"b": date_range("1/1/2001", periods=2)})
    with tm.assert_produces_warning(None):
        result = getattr(df, opname)()
    assert isinstance(result, Series)

    df["a"] = range(len(df))
    with tm.assert_produces_warning(None):
        result = getattr(df, opname)()
    assert isinstance(result, Series)
    assert len(result)

if has_skipna:

    def wrapper(x):
        exit(alternative(x.values))

    skipna_wrapper = tm._make_skipna_wrapper(alternative, skipna_alternative)
    result0 = f(axis=0, skipna=False)
    result1 = f(axis=1, skipna=False)
    tm.assert_series_equal(
        result0, frame.apply(wrapper), check_dtype=check_dtype, rtol=rtol, atol=atol
    )
    tm.assert_series_equal(
        result1,
        frame.apply(wrapper, axis=1),
        rtol=rtol,
        atol=atol,
    )
else:
    skipna_wrapper = alternative

result0 = f(axis=0)
result1 = f(axis=1)
tm.assert_series_equal(
    result0,
    frame.apply(skipna_wrapper),
    check_dtype=check_dtype,
    rtol=rtol,
    atol=atol,
)

if opname in ["sum", "prod"]:
    expected = frame.apply(skipna_wrapper, axis=1)
    tm.assert_series_equal(
        result1, expected, check_dtype=False, rtol=rtol, atol=atol
    )

# check dtypes
if check_dtype:
    lcd_dtype = frame.values.dtype
    assert lcd_dtype == result0.dtype
    assert lcd_dtype == result1.dtype

# bad axis
with pytest.raises(ValueError, match="No axis named 2"):
    f(axis=2)

# all NA case
if has_skipna:
    all_na = frame * np.NaN
    r0 = getattr(all_na, opname)(axis=0)
    r1 = getattr(all_na, opname)(axis=1)
    if opname in ["sum", "prod"]:
        unit = 1 if opname == "prod" else 0  # result for empty sum/prod
        expected = Series(unit, index=r0.index, dtype=r0.dtype)
        tm.assert_series_equal(r0, expected)
        expected = Series(unit, index=r1.index, dtype=r1.dtype)
        tm.assert_series_equal(r1, expected)
