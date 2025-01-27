# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_timedelta.py
# ndarray.item() incorrectly returns int for dt64[ns] and td64[ns]
dt64 = fixed_now_ts.to_datetime64()
arg = np.array(dt64)

msg = (
    "Value must be Timedelta, string, integer, float, timedelta "
    "or convertible, not datetime64"
)
with pytest.raises(ValueError, match=msg):
    to_timedelta(arg)

arg2 = arg.view("m8[ns]")
result = to_timedelta(arg2)
assert isinstance(result, pd.Timedelta)
assert result.value == dt64.view("i8")
