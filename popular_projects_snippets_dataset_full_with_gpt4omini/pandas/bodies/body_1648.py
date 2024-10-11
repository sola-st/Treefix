# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH 16309
result = DataFrame(columns=["time", "value"])
result.loc[1] = {"time": Timedelta(6, unit="s"), "value": "foo"}
result.loc[1] = {"time": Timedelta(6, unit="s"), "value": "foo"}
expected = DataFrame(
    [[Timedelta(6, unit="s"), "foo"]], columns=["time", "value"], index=[1]
)
tm.assert_frame_equal(result, expected)
