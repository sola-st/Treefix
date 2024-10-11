# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_concat.py
# https://github.com/pandas-dev/pandas/issues/25257
df = pd.DataFrame(
    {"timestamp": [pd.Timestamp("2020-04-08 09:00:00.709949+0000", tz="UTC")]}
)
expected = df.copy()
result = pd.concat([df], copy=copy)
tm.assert_frame_equal(result, expected)
