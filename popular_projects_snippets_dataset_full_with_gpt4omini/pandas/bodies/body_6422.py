# Extracted from ./data/repos/pandas/pandas/tests/extension/test_interval.py
N = 100
left_array = np.random.uniform(size=N).cumsum()
right_array = left_array + np.random.uniform(size=N)
exit([Interval(left, right) for left, right in zip(left_array, right_array)])
