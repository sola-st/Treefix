# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
if not is_platform_little_endian():
    pytest.skip("known failure on non-little endian")

data = pd.read_pickle(legacy_pickle)

for typ, dv in data.items():
    for dt, result in dv.items():
        expected = data[typ][dt]

        if typ == "series" and dt == "ts":
            # GH 7748
            tm.assert_series_equal(result, expected)
            assert result.index.freq == expected.index.freq
            assert not result.index.freq.normalize
            tm.assert_series_equal(result > 0, expected > 0)

            # GH 9291
            freq = result.index.freq
            assert freq + Day(1) == Day(2)

            res = freq + pd.Timedelta(hours=1)
            assert isinstance(res, pd.Timedelta)
            assert res == pd.Timedelta(days=1, hours=1)

            res = freq + pd.Timedelta(nanoseconds=1)
            assert isinstance(res, pd.Timedelta)
            assert res == pd.Timedelta(days=1, nanoseconds=1)
        elif typ == "index" and dt == "period":
            tm.assert_index_equal(result, expected)
            assert isinstance(result.freq, MonthEnd)
            assert result.freq == MonthEnd()
            assert result.freqstr == "M"
            tm.assert_index_equal(result.shift(2), expected.shift(2))
        elif typ == "series" and dt in ("dt_tz", "cat"):
            tm.assert_series_equal(result, expected)
        elif typ == "frame" and dt in (
            "dt_mixed_tzs",
            "cat_onecol",
            "cat_and_float",
        ):
            tm.assert_frame_equal(result, expected)
        else:
            compare_element(result, expected, typ)
