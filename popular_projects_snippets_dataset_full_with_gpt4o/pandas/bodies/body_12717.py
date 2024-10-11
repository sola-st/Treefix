# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
encoding = ujson.encode(bigNum)
assert str(bigNum) == encoding

with pytest.raises(
    ValueError,
    match="Value is too big|Value is too small",
):
    assert ujson.loads(encoding) == bigNum
