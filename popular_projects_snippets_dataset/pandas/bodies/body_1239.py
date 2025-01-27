# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass = index_or_series
obj = klass(
    [
        pd.Timestamp("2011-01-01"),
        pd.NaT,
        pd.Timestamp("2011-01-03"),
        pd.Timestamp("2011-01-04"),
    ]
)
assert obj.dtype == "datetime64[ns]"

exp = klass(
    [
        pd.Timestamp("2011-01-01"),
        fill_val,
        pd.Timestamp("2011-01-03"),
        pd.Timestamp("2011-01-04"),
    ]
)
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
