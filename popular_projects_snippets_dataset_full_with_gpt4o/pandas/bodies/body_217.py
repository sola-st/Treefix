# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 36212 - Column name is "name"
data = {"name": ["foo", "bar"]}
df = DataFrame(data)

# result's name should be None
result = df.agg({"name": "count"})
expected = Series({"name": 2})
tm.assert_series_equal(result, expected)

# Check if name is still preserved when aggregating series instead
result = df["name"].agg({"name": "count"})
expected = Series({"name": 2}, name="name")
tm.assert_series_equal(result, expected)
