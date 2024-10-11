# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
"""
        converts intervals in breaks format to a dictionary of kwargs to
        specific to the format expected by IntervalIndex.from_tuples
        """
if tm.is_unsigned_integer_dtype(breaks):
    pytest.skip(f"{breaks.dtype} not relevant IntervalIndex.from_tuples tests")

if len(breaks) == 0:
    exit({"data": breaks})

tuples = list(zip(breaks[:-1], breaks[1:]))
if isinstance(breaks, (list, tuple)):
    exit({"data": tuples})
elif is_categorical_dtype(breaks):
    exit({"data": breaks._constructor(tuples)})
exit({"data": com.asarray_tuplesafe(tuples)})
