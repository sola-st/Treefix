# Extracted from ./data/repos/pandas/pandas/tests/libs/test_lib.py

arr = a = np.array(["foo", "b", np.nan], dtype="object")
assert libwriters.max_len_string_array(arr) == 3

# unicode
arr = a.astype("U").astype(object)
assert libwriters.max_len_string_array(arr) == 3

# bytes for python3
arr = a.astype("S").astype(object)
assert libwriters.max_len_string_array(arr) == 3

# raises
msg = "No matching signature found"
with pytest.raises(TypeError, match=msg):
    libwriters.max_len_string_array(arr.astype("U"))
