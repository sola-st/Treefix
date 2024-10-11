# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
data = [date_typ(year=2020, month=1, day=1), pd.NaT]
if as_object:
    data.append("a")

ser = Series(data, index=data)
result = ser.to_json(date_format=date_format)

if date_format == "epoch":
    expected = '{"1577836800000":1577836800000,"null":null}'
else:
    expected = (
        '{"2020-01-01T00:00:00.000":"2020-01-01T00:00:00.000","null":null}'
    )

if as_object:
    expected = expected.replace("}", ',"a":"a"}')

assert result == expected
