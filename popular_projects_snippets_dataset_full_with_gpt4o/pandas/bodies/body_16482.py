# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH#41951
df = DataFrame([["id", 2, 3]], columns=["a", "b", "b"])
result = df.melt(id_vars=["a"], value_vars=["b"])
expected = DataFrame(
    [["id", "b", 2], ["id", "b", 3]], columns=["a", "variable", "value"]
)
tm.assert_frame_equal(result, expected)
