# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_period_asfreq.py
# with non-object, make sure we raise TypeError, not segfault
arr = np.arange(5)
freq = to_offset("D")
with pytest.raises(TypeError, match="values must be object-dtype"):
    extract_ordinals(arr, freq)
