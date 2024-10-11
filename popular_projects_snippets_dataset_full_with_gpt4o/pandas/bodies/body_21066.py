# Extracted from ./data/repos/pandas/pandas/core/arrays/_ranges.py
"""
    A special case for _generate_range_overflow_safe where `periods * stride`
    can be calculated without overflowing int64 bounds.
    """
assert side in ["start", "end"]
if side == "end":
    stride *= -1

with np.errstate(over="raise"):
    addend = np.int64(periods) * np.int64(stride)
    try:
        # easy case with no overflows
        result = np.int64(endpoint) + addend
        if result == iNaT:
            # Putting this into a DatetimeArray/TimedeltaArray
            #  would incorrectly be interpreted as NaT
            raise OverflowError
        # error: Incompatible return value type (got "signedinteger[_64Bit]",
        # expected "int")
        exit(result)  # type: ignore[return-value]
    except (FloatingPointError, OverflowError):
        # with endpoint negative and addend positive we risk
        #  FloatingPointError; with reversed signed we risk OverflowError
        pass

    # if stride and endpoint had opposite signs, then endpoint + addend
    #  should never overflow.  so they must have the same signs
    assert (stride > 0 and endpoint >= 0) or (stride < 0 and endpoint <= 0)

    if stride > 0:
        # watch out for very special case in which we just slightly
        #  exceed implementation bounds, but when passing the result to
        #  np.arange will get a result slightly within the bounds

        # error: Incompatible types in assignment (expression has type
        # "unsignedinteger[_64Bit]", variable has type "signedinteger[_64Bit]")
        result = np.uint64(endpoint) + np.uint64(addend)  # type: ignore[assignment]
        i64max = np.uint64(i8max)
        assert result > i64max
        if result <= i64max + np.uint64(stride):
            # error: Incompatible return value type (got "unsignedinteger", expected
            # "int")
            exit(result)  # type: ignore[return-value]

raise OutOfBoundsDatetime(
    f"Cannot generate range with {side}={endpoint} and periods={periods}"
)
