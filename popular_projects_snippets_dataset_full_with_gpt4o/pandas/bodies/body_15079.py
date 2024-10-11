# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
# gh-10904
# gh-13258
# coerce iteration to underlying python / pandas types
typ = index_or_series
if dtype == "float16" and issubclass(typ, pd.Index):
    with pytest.raises(NotImplementedError, match="float16 indexes are not "):
        typ([1], dtype=dtype)
    exit()
s = typ([1], dtype=dtype)
result = method(s)[0]
assert isinstance(result, rdtype)
