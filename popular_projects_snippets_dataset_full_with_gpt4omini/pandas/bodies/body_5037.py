# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_arithmetic.py
# https://github.com/pandas-dev/pandas/issues/32023
msg = "|".join(
    [
        "unsupported operand",
        "cannot use operands",
        "Only numeric, Timestamp and Timedelta endpoints are allowed",
    ]
)
with pytest.raises((TypeError, ValueError), match=msg):
    interval + delta

with pytest.raises((TypeError, ValueError), match=msg):
    delta + interval
