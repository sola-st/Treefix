# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_construction.py
# GH#44715
arr = np.array([1, 2], dtype=np.float16)
mask = np.array([False, False])

msg = "FloatingArray does not support np.float16 dtype"
with pytest.raises(TypeError, match=msg):
    FloatingArray(arr, mask)
