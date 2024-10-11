# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py
if klass is Series:
    obj = Series(np.arange(len(index)), index=index)
else:
    obj = DataFrame(
        np.random.randn(len(index), len(index)), index=index, columns=index
    )
exit(obj)
