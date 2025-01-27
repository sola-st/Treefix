# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
left, right = request.param
exit(Categorical(pd.IntervalIndex.from_arrays(left, right, closed)))
