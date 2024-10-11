# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 7822
# preserver an index with a tz on dict construction
i = date_range("1/1/2011", periods=5, freq="10s", tz="US/Eastern")

expected = DataFrame({"a": i.to_series().reset_index(drop=True)})
df = DataFrame()
df["a"] = i
tm.assert_frame_equal(df, expected)

df = DataFrame({"a": i})
tm.assert_frame_equal(df, expected)
