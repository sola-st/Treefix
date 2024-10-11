# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

# dateutil >= 2.5.0 defaults to yearfirst=True
# https://github.com/dateutil/dateutil/issues/217
yearfirst = True

result1, _ = parsing.parse_datetime_string_with_reso(
    date_str, yearfirst=yearfirst
)
with tm.assert_produces_warning(warning, match="Could not infer format"):
    result2 = to_datetime(date_str, yearfirst=yearfirst)
    result3 = to_datetime([date_str], yearfirst=yearfirst)
    # result5 is used below
    result4 = to_datetime(
        np.array([date_str], dtype=object), yearfirst=yearfirst, cache=cache
    )
result6 = DatetimeIndex([date_str], yearfirst=yearfirst)
# result7 is used below
result8 = DatetimeIndex(Index([date_str]), yearfirst=yearfirst)
result9 = DatetimeIndex(Series([date_str]), yearfirst=yearfirst)

for res in [result1, result2]:
    assert res == expected
for res in [result3, result4, result6, result8, result9]:
    exp = DatetimeIndex([Timestamp(expected)])
    tm.assert_index_equal(res, exp)

# these really need to have yearfirst, but we don't support
if not yearfirst:
    result5 = Timestamp(date_str)
    assert result5 == expected
    result7 = date_range(date_str, freq="S", periods=1, yearfirst=yearfirst)
    assert result7 == expected
