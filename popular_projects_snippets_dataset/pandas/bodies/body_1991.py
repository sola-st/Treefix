# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# see gh-24910
#
# Even if we discover that we have to hold float, does not mean
# we should be lenient on subsequent elements that fail to be integer.
kwargs = {"errors": errors} if errors is not None else {}
arr = [str(-large_val if signed else large_val)]

if multiple_elts:
    arr.insert(0, large_val)

if errors in (None, "raise"):
    index = int(multiple_elts)
    msg = f"Integer out of range. at position {index}"

    with pytest.raises(ValueError, match=msg):
        to_numeric(arr, **kwargs)
else:
    result = to_numeric(arr, **kwargs)

    if errors == "coerce":
        expected = [float(i) for i in arr]
        exp_dtype = float
    else:
        expected = arr
        exp_dtype = object

    tm.assert_almost_equal(result, np.array(expected, dtype=exp_dtype))
