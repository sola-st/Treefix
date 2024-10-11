# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
vals = np.random.randn(5, 3)
f = lambda x: pd.DataFrame(
    x, index=list("ABCDE"), columns=["jim", "joe", "jolie"]
)

df = f(vals)

tm.assert_frame_equal(df / np.array(other), f(vals / other))
tm.assert_frame_equal(np.array(other) * df, f(vals * other))
tm.assert_frame_equal(df + np.array(other), f(vals + other))
tm.assert_frame_equal(np.array(other) - df, f(other - vals))
