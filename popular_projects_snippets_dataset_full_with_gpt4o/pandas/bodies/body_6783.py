# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
# GH 21670
index = interval_range(0, 5)
msg = f"invalid option for 'closed': {bad_closed}"
with pytest.raises(ValueError, match=msg):
    index.set_closed(bad_closed)
