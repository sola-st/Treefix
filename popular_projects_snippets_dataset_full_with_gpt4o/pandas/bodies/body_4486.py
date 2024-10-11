# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# multiples
i = date_range("1/1/2011", periods=5, freq="10s", tz="US/Eastern")
i_no_tz = date_range("1/1/2011", periods=5, freq="10s")
df = DataFrame({"a": i, "b": i_no_tz})
expected = DataFrame({"a": i.to_series().reset_index(drop=True), "b": i_no_tz})
tm.assert_frame_equal(df, expected)
