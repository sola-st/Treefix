# Extracted from ./data/repos/pandas/pandas/tests/frame/test_query_eval.py
# https://github.com/pandas-dev/pandas/issues/29463
tz = tz_aware_fixture
df_index = date_range(
    start="2019-01-01", freq="1d", periods=10, tz=tz, name="time"
)
expected = DataFrame(index=df_index)
df = DataFrame(index=df_index)
result = df.query('"2018-01-03 00:00:00+00" < time')
tm.assert_frame_equal(result, expected)

expected = DataFrame(df_index)
result = df.reset_index().query('"2018-01-03 00:00:00+00" < time')
tm.assert_frame_equal(result, expected)
