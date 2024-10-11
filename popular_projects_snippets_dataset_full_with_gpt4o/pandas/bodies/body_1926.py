# Extracted from ./data/repos/pandas/pandas/tests/resample/test_period_index.py
# 4076
# when the frequency is evenly divisible, sometimes extra bins

df = DataFrame(np.random.randn(9, 3), index=date_range("2000-1-1", periods=9))
result = df.resample("5D").mean()
expected = pd.concat([df.iloc[0:5].mean(), df.iloc[5:].mean()], axis=1).T
expected.index = pd.DatetimeIndex(
    [Timestamp("2000-1-1"), Timestamp("2000-1-6")], freq="5D"
)
tm.assert_frame_equal(result, expected)

index = date_range(start="2001-5-4", periods=28)
df = DataFrame(
    [
        {
            "REST_KEY": 1,
            "DLY_TRN_QT": 80,
            "DLY_SLS_AMT": 90,
            "COOP_DLY_TRN_QT": 30,
            "COOP_DLY_SLS_AMT": 20,
        }
    ]
    * 28
    + [
        {
            "REST_KEY": 2,
            "DLY_TRN_QT": 70,
            "DLY_SLS_AMT": 10,
            "COOP_DLY_TRN_QT": 50,
            "COOP_DLY_SLS_AMT": 20,
        }
    ]
    * 28,
    index=index.append(index),
).sort_index()

index = date_range("2001-5-4", periods=4, freq="7D")
expected = DataFrame(
    [
        {
            "REST_KEY": 14,
            "DLY_TRN_QT": 14,
            "DLY_SLS_AMT": 14,
            "COOP_DLY_TRN_QT": 14,
            "COOP_DLY_SLS_AMT": 14,
        }
    ]
    * 4,
    index=index,
)
result = df.resample("7D").count()
tm.assert_frame_equal(result, expected)

expected = DataFrame(
    [
        {
            "REST_KEY": 21,
            "DLY_TRN_QT": 1050,
            "DLY_SLS_AMT": 700,
            "COOP_DLY_TRN_QT": 560,
            "COOP_DLY_SLS_AMT": 280,
        }
    ]
    * 4,
    index=index,
)
result = df.resample("7D").sum()
tm.assert_frame_equal(result, expected)
