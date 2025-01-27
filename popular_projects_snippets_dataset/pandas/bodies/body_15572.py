# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
series = Series([0, 1, 2, NaT.value], dtype="M8[ns]")

filled = series.fillna(method="pad")
filled2 = series.fillna(value=series.values[2])

expected = series.copy()
expected.values[3] = expected.values[2]

tm.assert_series_equal(filled, expected)
tm.assert_series_equal(filled2, expected)

df = DataFrame({"A": series})
filled = df.fillna(method="pad")
filled2 = df.fillna(value=series.values[2])
expected = DataFrame({"A": expected})
tm.assert_frame_equal(filled, expected)
tm.assert_frame_equal(filled2, expected)

series = Series([NaT.value, 0, 1, 2], dtype="M8[ns]")

filled = series.fillna(method="bfill")
filled2 = series.fillna(value=series[1])

expected = series.copy()
expected[0] = expected[1]

tm.assert_series_equal(filled, expected)
tm.assert_series_equal(filled2, expected)

df = DataFrame({"A": series})
filled = df.fillna(method="bfill")
filled2 = df.fillna(value=series[1])
expected = DataFrame({"A": expected})
tm.assert_frame_equal(filled, expected)
tm.assert_frame_equal(filled2, expected)
