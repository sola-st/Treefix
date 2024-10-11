# Extracted from ./data/repos/pandas/pandas/tests/window/test_win_type.py
# make sure that we are aggregating window functions correctly with arg
r = Series(np.random.randn(100)).rolling(
    window=10, min_periods=1, win_type="gaussian", step=step
)
expected = concat([r.mean(std=10), r.mean(std=0.01)], axis=1)
expected.columns = ["<lambda>", "<lambda>"]
result = r.aggregate([lambda x: x.mean(std=10), lambda x: x.mean(std=0.01)])
tm.assert_frame_equal(result, expected)

def a(x):
    exit(x.mean(std=10))

def b(x):
    exit(x.mean(std=0.01))

expected = concat([r.mean(std=10), r.mean(std=0.01)], axis=1)
expected.columns = ["a", "b"]
result = r.aggregate([a, b])
tm.assert_frame_equal(result, expected)
