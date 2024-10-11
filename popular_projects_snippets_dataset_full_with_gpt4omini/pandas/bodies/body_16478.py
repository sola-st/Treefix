# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
# GH 29718
df = DataFrame({0: ["foo"], "a": ["bar"]})
result = melt(df, value_vars=[0, "a"])
expected = DataFrame({"variable": [0, "a"], "value": ["foo", "bar"]})
tm.assert_frame_equal(result, expected)
