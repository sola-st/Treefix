# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
klass = index_or_series
tz = "US/Eastern"

obj = klass(
    [
        pd.Timestamp("2011-01-01", tz=tz),
        pd.NaT,
        pd.Timestamp("2011-01-03", tz=tz),
        pd.Timestamp("2011-01-04", tz=tz),
    ]
)
assert obj.dtype == "datetime64[ns, US/Eastern]"

if getattr(fill_val, "tz", None) is None:
    fv = fill_val
else:
    fv = fill_val.tz_convert(tz)
exp = klass(
    [
        pd.Timestamp("2011-01-01", tz=tz),
        fv,
        pd.Timestamp("2011-01-03", tz=tz),
        pd.Timestamp("2011-01-04", tz=tz),
    ]
)
self._assert_fillna_conversion(obj, fill_val, exp, fill_dtype)
