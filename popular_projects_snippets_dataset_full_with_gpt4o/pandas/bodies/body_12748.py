# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
# gh-18878
msg = re.escape("array(1) (0d array) is not JSON serializable at the moment")
with pytest.raises(TypeError, match=msg):
    ujson.encode(np.array(1))
