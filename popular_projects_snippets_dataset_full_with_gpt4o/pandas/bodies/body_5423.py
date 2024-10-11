# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
assert (
    int(
        np.round(Timestamp(x).value / 1e9)
        - np.round(Timestamp(y).value / 1e9)
    )
    == 0
)
