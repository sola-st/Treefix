# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_describe.py
# GH#32409
df = DataFrame([{"test": {"a": "1"}}, {"test": {"a": "2"}}])
expected = DataFrame(
    {"test": [2, 2, {"a": "1"}, 1]}, index=["count", "unique", "top", "freq"]
)
result = df.describe()
tm.assert_frame_equal(result, expected)
