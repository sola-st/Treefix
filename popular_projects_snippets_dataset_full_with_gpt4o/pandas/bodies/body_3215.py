# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asfreq.py
# GH#39805
# Test that rows are not dropped when the datetime index is out of order
index = to_datetime(["2021-01-04", "2021-01-02", "2021-01-03", "2021-01-01"])
result = frame_or_series(range(4), index=index)

expected = result.reindex(sorted(index))
expected.index = expected.index._with_freq("infer")

result = result.asfreq("D")
tm.assert_equal(result, expected)
