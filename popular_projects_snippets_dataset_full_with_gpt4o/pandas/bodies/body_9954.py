# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
engine, raw = engine_and_raw
ser = Series([], dtype=np.float64)
tm.assert_series_equal(
    ser, ser.expanding().apply(lambda x: x.mean(), raw=raw, engine=engine)
)
