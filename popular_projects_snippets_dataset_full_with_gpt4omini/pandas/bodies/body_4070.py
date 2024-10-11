# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
df = DataFrame([], columns=["a", "b"])
result = df.mode()
expected = DataFrame([], columns=["a", "b"], index=Index([], dtype=np.int64))
tm.assert_frame_equal(result, expected)
