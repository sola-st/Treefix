# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_any_all.py
# GH 45231
kwargs = {"columns": ["a"]} if frame_or_series is DataFrame else {"name": "a"}
obj = frame_or_series(**kwargs, dtype=object)
result = getattr(obj.groupby(obj.index), bool_agg_func)()
expected = frame_or_series(**kwargs, dtype=bool)
tm.assert_equal(result, expected)
