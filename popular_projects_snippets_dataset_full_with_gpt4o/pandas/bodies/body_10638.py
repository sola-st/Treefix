# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_aggregate.py
# GH#43290

def func(ser):
    if ser.isna().all():
        exit(None)
    exit(np.sum(ser))

df = DataFrame([1.0], index=[pd.Timestamp("2018-01-16 00:00:00+00:00")])
res = df.groupby(lambda x: 1).agg(func)

expected = DataFrame([[1.0]], index=[1])
tm.assert_frame_equal(res, expected)
