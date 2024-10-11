# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# we are trying to transform with an aggregator
with pytest.raises(ValueError, match=msg):
    with np.errstate(all="ignore"):
        string_series.agg(func)
