# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_astype.py
msg = "data type [\"']fake_dtype[\"'] not understood"
with pytest.raises(TypeError, match=msg):
    index.astype("fake_dtype")
