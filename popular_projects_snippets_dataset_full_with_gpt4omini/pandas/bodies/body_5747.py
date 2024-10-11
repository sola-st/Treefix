# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# In the base class we expect data.dtype.type; but this (intentionally)
#  returns Python scalars or pd.NA
pa_type = data._data.type
if pa.types.is_integer(pa_type):
    exp_type = int
elif pa.types.is_floating(pa_type):
    exp_type = float
elif pa.types.is_string(pa_type):
    exp_type = str
elif pa.types.is_binary(pa_type):
    exp_type = bytes
elif pa.types.is_boolean(pa_type):
    exp_type = bool
elif pa.types.is_duration(pa_type):
    exp_type = timedelta
elif pa.types.is_timestamp(pa_type):
    if pa_type.unit == "ns":
        exp_type = pd.Timestamp
    else:
        exp_type = datetime
elif pa.types.is_date(pa_type):
    exp_type = date
elif pa.types.is_time(pa_type):
    exp_type = time
else:
    raise NotImplementedError(data.dtype)

result = data[0]
assert isinstance(result, exp_type), type(result)

result = pd.Series(data)[0]
assert isinstance(result, exp_type), type(result)
