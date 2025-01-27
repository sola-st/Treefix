# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# GH#45241
# TODO: make an extension interface test for this?
arr = interval_range(1, 10.0)._values
df = DataFrame(arr)

# ser should be a *view* on the DataFrame data
ser = df.iloc[2]

# if we have a view, then changing arr[2] should also change ser[0]
assert arr[2] != arr[-1]  # otherwise the rest isn't meaningful
arr[2] = arr[-1]
assert ser[0] == arr[-1]
