# Extracted from ./data/repos/pandas/pandas/tests/util/test_hashing.py
msg = "Unexpected type for hashing"
with pytest.raises(TypeError, match=msg):
    hash_pandas_object(pd.Timestamp("20130101"))
