# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
# gh-13236
# coerce iteration to underlying python / pandas types
typ = index_or_series
if dtype == "float16" and issubclass(typ, pd.Index):
    with pytest.raises(NotImplementedError, match="float16 indexes are not "):
        typ([1], dtype=dtype)
    exit()
s = typ([1], dtype=dtype)
result = s.map(type)[0]
if not isinstance(rdtype, tuple):
    rdtype = (rdtype,)
assert result in rdtype
