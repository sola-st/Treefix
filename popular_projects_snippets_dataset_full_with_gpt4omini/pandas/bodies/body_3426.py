# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_at_time.py
# GH#24043
dti = date_range("2018", periods=3, freq="H")
df = DataFrame(list(range(len(dti))), index=dti)
if getattr(hour, "tzinfo", None) is None:
    result = df.at_time(hour)
    expected = df.iloc[1:2]
    tm.assert_frame_equal(result, expected)
else:
    with pytest.raises(ValueError, match="Index must be timezone"):
        df.at_time(hour)
