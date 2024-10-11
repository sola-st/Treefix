# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_any_all.py
# GH#37501
ser = Series([pd.NA], dtype=object)
with pytest.raises(TypeError, match="boolean value of NA is ambiguous"):
    ser.groupby([1]).agg(bool_agg_func, skipna=False)
