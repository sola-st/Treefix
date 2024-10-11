# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
# GH 9952
df = pd.DataFrame(
    {"a": np.random.randn(6)},
    index=pd.MultiIndex.from_product(
        [["a", "b"], [0, 1, 2]], names=["levA", "levB"]
    ),
)
df2 = df.copy()
df2.index = df2.index.swaplevel(0, 1)
result = df - df2
expected = pd.DataFrame([0.0] * 6, columns=["a"], index=df.index)
tm.assert_frame_equal(result, expected)
