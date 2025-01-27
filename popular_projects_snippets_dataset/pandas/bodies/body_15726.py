# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_csv.py

with tm.ensure_clean() as filename:
    ser = Series([0.123456, 0.234567, 0.567567])
    ser.to_csv(filename, float_format="%.2f", header=False)

    rs = self.read_csv(filename)
    xp = Series([0.12, 0.23, 0.57])
    tm.assert_series_equal(rs, xp)
