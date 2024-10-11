# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
rng = list(
    generate_range(
        start=datetime(2008, 1, 1),
        end=datetime(2008, 1, 3),
        periods=None,
        offset=BDay(),
        unit="ns",
    )
)
expected = [datetime(2008, 1, 1), datetime(2008, 1, 2), datetime(2008, 1, 3)]
assert rng == expected
