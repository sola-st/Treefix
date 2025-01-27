# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH#22558
df1 = DataFrame(test)
expected = Series(data=constant, index=["a", "b"], dtype="object")
aggregation = {"a": "unique", "b": "unique"}

result = df1.agg(aggregation)

tm.assert_series_equal(result, expected)
