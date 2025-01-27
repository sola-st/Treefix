# Extracted from ./data/repos/pandas/pandas/tests/base/test_unique.py
obj = index_or_series_obj

if not allow_na_ops(obj):
    pytest.skip("type doesn't allow for NA operations")
elif isinstance(obj, pd.MultiIndex):
    pytest.skip(f"MultiIndex can't hold '{null_obj}'")

values = obj._values
values[0:2] = null_obj

klass = type(obj)
repeated_values = np.repeat(values, range(1, len(values) + 1))
obj = klass(repeated_values, dtype=obj.dtype)

if isinstance(obj, pd.CategoricalIndex):
    assert obj.nunique() == len(obj.categories)
    assert obj.nunique(dropna=False) == len(obj.categories) + 1
else:
    num_unique_values = len(obj.unique())
    assert obj.nunique() == max(0, num_unique_values - 1)
    assert obj.nunique(dropna=False) == max(0, num_unique_values)
