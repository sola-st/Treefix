# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# https://github.com/pandas-dev/pandas/issues/35471
df = DataFrame(Series(data, dtype=dtype))
if errors == "ignore":
    expected = df
    result = df.astype(float, errors=errors)
    tm.assert_frame_equal(result, expected)
else:
    msg = "(Cannot cast)|(could not convert)"
    with pytest.raises((ValueError, TypeError), match=msg):
        df.astype(float, errors=errors)
