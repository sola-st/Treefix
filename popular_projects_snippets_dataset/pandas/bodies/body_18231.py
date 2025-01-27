# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_numeric.py
frame = float_frame

garbage = np.random.random(4)
colSeries = Series(garbage, index=np.array(frame.columns))

idSum = frame + frame
seriesSum = frame + colSeries

for col, series in idSum.items():
    for idx, val in series.items():
        origVal = frame[col][idx] * 2
        if not np.isnan(val):
            assert val == origVal
        else:
            assert np.isnan(origVal)

for col, series in seriesSum.items():
    for idx, val in series.items():
        origVal = frame[col][idx] + colSeries[col]
        if not np.isnan(val):
            assert val == origVal
        else:
            assert np.isnan(origVal)
