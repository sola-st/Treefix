# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
mi = pd.MultiIndex.from_product([np.arange(5), np.arange(5)])
with pytest.raises(TypeError, match="Cannot create a DatetimeArray"):
    DatetimeArray._from_sequence(mi)
