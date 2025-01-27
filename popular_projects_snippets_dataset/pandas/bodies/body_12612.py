# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH28156: to_json not correctly formatting Timedelta
data = [timedelta_typ(days=1), timedelta_typ(days=2), pd.NaT]
if as_object:
    data.append("a")

ser = Series(data, index=data)
if date_format == "iso":
    expected = (
        '{"P1DT0H0M0S":"P1DT0H0M0S","P2DT0H0M0S":"P2DT0H0M0S","null":null}'
    )
else:
    expected = '{"86400000":86400000,"172800000":172800000,"null":null}'

if as_object:
    expected = expected.replace("}", ',"a":"a"}')

result = ser.to_json(date_format=date_format)
assert result == expected
