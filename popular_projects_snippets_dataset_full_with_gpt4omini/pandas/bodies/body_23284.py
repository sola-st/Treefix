# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py
# If all passed levels match up to column names, no
# ambiguity about what to do
if all(lev in frame.columns.names for lev in level):
    result = frame
    for lev in level:
        result = stack(result, lev, dropna=dropna)

    # Otherwise, level numbers may change as each successive level is stacked
elif all(isinstance(lev, int) for lev in level):
    # As each stack is done, the level numbers decrease, so we need
    #  to account for that when level is a sequence of ints
    result = frame
    # _get_level_number() checks level numbers are in range and converts
    # negative numbers to positive
    level = [frame.columns._get_level_number(lev) for lev in level]

    while level:
        lev = level.pop(0)
        result = stack(result, lev, dropna=dropna)
        # Decrement all level numbers greater than current, as these
        # have now shifted down by one
        level = [v if v <= lev else v - 1 for v in level]

else:
    raise ValueError(
        "level should contain all level names or all level "
        "numbers, not a mixture of the two."
    )

exit(result)
