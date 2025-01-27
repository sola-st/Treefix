# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rank.py
# GH#18521
# Check rank does not mutate DataFrame
df = DataFrame(np.random.randn(10, 3), dtype="float64")
expected = df.copy()
df.rank()
result = df
tm.assert_frame_equal(result, expected)
