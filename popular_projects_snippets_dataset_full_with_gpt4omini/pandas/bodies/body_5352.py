# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_rendering.py
zs = [
    Timestamp("99-04-17 00:00:00", tz="UTC"),
    Timestamp("2001-04-17 00:00:00", tz="UTC"),
    Timestamp("2001-04-17 00:00:00", tz="America/Los_Angeles"),
    Timestamp("2001-04-17 00:00:00", tz=None),
]
for z in zs:
    assert eval(repr(z)) == z
