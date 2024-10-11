# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_asof.py
# GH21194
# Testing awareness of DataFrame index considering different
# UTC and timezone
df = DataFrame(
    data=[1, 2],
    index=[
        Timestamp("2018-01-01 21:00:05.001+00:00"),
        Timestamp("2018-01-01 22:35:10.550+00:00"),
    ],
)

result = df.asof(stamp)
tm.assert_series_equal(result, expected)
