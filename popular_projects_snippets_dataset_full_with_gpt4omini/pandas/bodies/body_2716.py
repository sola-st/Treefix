# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_select_dtypes.py
# GH 35340

df = DataFrame(arr)
is_selected = df.select_dtypes(np.number).shape == df.shape
assert is_selected == expected
