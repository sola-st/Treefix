# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
rng = list(
    generate_range(
        start=datetime(2008, 1, 5),
        end=datetime(2008, 1, 6),
        periods=None,
        offset=BDay(),
        unit="ns",
    )
)
expected = []
assert rng == expected
