# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
idx = DatetimeIndex(np.array([], dtype=f"datetime64[{unit}]"))
assert len(idx) == 0
