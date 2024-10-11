# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
rng = list(
    generate_range(
        start=datetime(2009, 3, 25),
        end=None,
        periods=2,
        offset=BDay(),
        unit="ns",
    )
)
expected = [datetime(2009, 3, 25), datetime(2009, 3, 26)]
assert rng == expected
