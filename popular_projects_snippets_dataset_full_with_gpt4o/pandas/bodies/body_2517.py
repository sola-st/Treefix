# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
arr = np.random.randn(len(float_frame))

float_frame[dtype] = np.array(arr, dtype=dtype)
assert float_frame[dtype].dtype.name == dtype
