# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_select_dtypes.py
arr = pd.array(["a", "b"], dtype=nullable_string_dtype)
df = DataFrame(arr)
is_selected = df.select_dtypes(np.number).shape == df.shape
assert not is_selected
