# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/common.py
actual = offset + base
actual_swapped = base + offset
actual_apply = offset._apply(base)
try:
    assert actual == expected
    assert actual_swapped == expected
    assert actual_apply == expected
except AssertionError as err:
    raise AssertionError(
        f"\nExpected: {expected}\nActual: {actual}\nFor Offset: {offset})"
        f"\nAt Date: {base}"
    ) from err
