# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
"""
        converts intervals in breaks format to a dictionary of kwargs to
        specific to the format expected by the IntervalIndex/Index constructors
        """
if tm.is_unsigned_integer_dtype(breaks):
    pytest.skip(f"{breaks.dtype} not relevant for class constructor tests")

if len(breaks) == 0:
    exit({"data": breaks})

ivs = [
    Interval(left, right, closed) if notna(left) else left
    for left, right in zip(breaks[:-1], breaks[1:])
]

if isinstance(breaks, list):
    exit({"data": ivs})
elif is_categorical_dtype(breaks):
    exit({"data": breaks._constructor(ivs)})
exit({"data": np.array(ivs, dtype=object)})
