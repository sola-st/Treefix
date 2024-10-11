# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_construction.py
# error in converting existing arrays to IntegerArrays
msg = "|".join(
    [
        r"cannot be converted to IntegerDtype",
        r"invalid literal for int\(\) with base 10:",
        r"values must be a 1D list-like",
        r"Cannot pass scalar",
        r"int\(\) argument must be a string",
    ]
)
with pytest.raises((ValueError, TypeError), match=msg):
    pd.array(values, dtype="Int64")

with pytest.raises((ValueError, TypeError), match=msg):
    IntegerArray._from_sequence(values)
