# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_to_period.py
offsets = ["MS", "BM"]
for off in offsets:
    rng = date_range("01-Jan-2012", periods=8, freq=off)
    prng = rng.to_period()
    assert prng.freq == "M"

rng = date_range("01-Jan-2012", periods=8, freq="M")
prng = rng.to_period()
assert prng.freq == "M"

with pytest.raises(ValueError, match=INVALID_FREQ_ERR_MSG):
    date_range("01-Jan-2012", periods=8, freq="EOM")
