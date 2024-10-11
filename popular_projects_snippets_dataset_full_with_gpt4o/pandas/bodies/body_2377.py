# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_insert.py
df = DataFrame(np.random.randn(4, 3))
ser = df[0]

if using_array_manager:
    expected_warning = None
else:
    # with BlockManager warn about high fragmentation of single dtype
    expected_warning = PerformanceWarning

with tm.assert_produces_warning(expected_warning):
    for n in range(100):
        df[n + 3] = df[1] * n

ser.values[0] = 99

assert df.iloc[0, 0] == df[0][0]
