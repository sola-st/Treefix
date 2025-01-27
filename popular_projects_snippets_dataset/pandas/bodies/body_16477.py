# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH 29718
df = DataFrame({0: ["foo"], "a": ["bar"], "b": [1], "d": [2]})
result = melt(df, id_vars=[0, "a"], value_vars=["b", "d"])
expected = DataFrame(
    {0: ["foo"] * 2, "a": ["bar"] * 2, "variable": list("bd"), "value": [1, 2]}
)
tm.assert_frame_equal(result, expected)
