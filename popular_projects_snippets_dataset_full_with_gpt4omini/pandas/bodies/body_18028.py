# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
# GH42003 TypeError instead of AttributeError
obj = pd.DatetimeIndex(["2018-10-28 01:20:00"], tz="Europe/Berlin")

msg = "Use hash_pandas_object instead"
with pytest.raises(TypeError, match=msg):
    hash_array(obj)
