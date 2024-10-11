# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
vals = [
    ["1 Day", "2 Days", "3 Days"],
    ["4 Days", "5 Days", "6 Days"],
]
df = DataFrame(vals, dtype=object)
msg = (
    r"Cannot convert from timedelta64\[ns\] to timedelta64\[.*\]. "
    "Supported resolutions are 's', 'ms', 'us', 'ns'"
)
with pytest.raises(ValueError, match=msg):
    # TODO: this is ValueError while for DatetimeArray it is TypeError;
    #  get these consistent
    df.astype(f"m8[{unit}]")
