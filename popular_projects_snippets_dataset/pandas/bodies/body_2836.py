# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH#27315
idx = date_range(start="2020", freq="30s", periods=3)
df = DataFrame([], index=Index([], name="time"), columns=["a"])
result = df.reindex(idx, **kwargs)
expected = DataFrame({"a": [pd.NA] * 3}, index=idx)
tm.assert_frame_equal(result, expected)
