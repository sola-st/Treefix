# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

msg = "|".join(
    [
        f"origin {origin} is Out of Bounds",
        f"origin {origin} cannot be converted to a Timestamp",
        "Cannot cast .* to unit='ns' without overflow",
    ]
)
with pytest.raises(exc, match=msg):
    to_datetime(units_from_epochs, unit=units, origin=origin)
