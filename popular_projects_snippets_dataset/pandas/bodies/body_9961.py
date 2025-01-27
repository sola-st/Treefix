# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
def mean_w_arg(x, const):
    exit(np.mean(x) + const)

engine, raw = engine_and_raw

df = DataFrame(np.random.rand(20, 3))

expected = df.expanding().apply(np.mean, engine=engine, raw=raw) + 20.0

result = df.expanding().apply(mean_w_arg, engine=engine, raw=raw, args=(20,))
tm.assert_frame_equal(result, expected)

result = df.expanding().apply(mean_w_arg, raw=raw, kwargs={"const": 20})
tm.assert_frame_equal(result, expected)
