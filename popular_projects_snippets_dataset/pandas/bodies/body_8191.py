# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
rng = date_range("1/1/2000 9:30", periods=10, freq="D", tz="US/Eastern")

result = rng.normalize()  # does not preserve freq
expected = date_range("1/1/2000", periods=10, freq="D", tz="US/Eastern")
tm.assert_index_equal(result, expected._with_freq(None))

assert result.is_normalized
assert not rng.is_normalized

rng = date_range("1/1/2000 9:30", periods=10, freq="D", tz="UTC")

result = rng.normalize()
expected = date_range("1/1/2000", periods=10, freq="D", tz="UTC")
tm.assert_index_equal(result, expected)

assert result.is_normalized
assert not rng.is_normalized

rng = date_range("1/1/2000 9:30", periods=10, freq="D", tz=tzlocal())
result = rng.normalize()  # does not preserve freq
expected = date_range("1/1/2000", periods=10, freq="D", tz=tzlocal())
tm.assert_index_equal(result, expected._with_freq(None))

assert result.is_normalized
assert not rng.is_normalized
