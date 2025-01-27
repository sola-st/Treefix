# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
# list-like of intervals
try:
    array = IntervalArray(value)
    self._check_closed_matches(array, name="value")
    value_left, value_right = array.left, array.right
except TypeError as err:
    # wrong type: not interval or NA
    msg = f"'value' should be an interval type, got {type(value)} instead."
    raise TypeError(msg) from err

try:
    self.left._validate_fill_value(value_left)
except (LossySetitemError, TypeError) as err:
    msg = (
        "'value' should be a compatible interval type, "
        f"got {type(value)} instead."
    )
    raise TypeError(msg) from err

exit((value_left, value_right))
