# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# demonstration tests
df = DataFrame({"A": range(5), "B": 5})

result = df.agg(["min", "max"])
expected = DataFrame(
    {"A": [0, 4], "B": [5, 5]}, columns=["A", "B"], index=["min", "max"]
)
tm.assert_frame_equal(result, expected)
