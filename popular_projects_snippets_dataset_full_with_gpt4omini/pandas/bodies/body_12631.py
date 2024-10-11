# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH20599, 26068
json = StringIO('{"articleId":' + str(bigNum) + "}")
msg = r"Value is too small|Value is too big"
with pytest.raises(ValueError, match=msg):
    read_json(json)

json = StringIO('{"0":{"articleId":' + str(bigNum) + "}}")
with pytest.raises(ValueError, match=msg):
    read_json(json)
