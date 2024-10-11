# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
fmt = "%Y-%m-%d %H:%M:%S %z"
date = "2010-01-01 12:00:00 " + offset

msg = "|".join(
    [
        r'^time data ".*" doesn\'t match format ".*", at position 0$',
        r'^unconverted data remains: ".*", at position 0$',
    ]
)
with pytest.raises(ValueError, match=msg):
    to_datetime([date], format=fmt)
