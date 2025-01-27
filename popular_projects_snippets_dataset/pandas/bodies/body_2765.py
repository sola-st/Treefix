# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
if frame_or_series is Series:
    arr = np.random.randn(10)
else:
    arr = np.random.randn(10, 10)
exit(frame_or_series(arr, dtype=None))
