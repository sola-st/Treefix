# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
msg = r"drop_duplicates\(\) got an unexpected keyword argument"
with pytest.raises(TypeError, match=msg):
    index.drop_duplicates(inplace=True)
