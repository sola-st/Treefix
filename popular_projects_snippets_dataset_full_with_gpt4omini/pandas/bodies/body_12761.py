# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
with pytest.raises(
    ValueError,
    match="Value is too big|Value is too small",
):
    ujson.loads(value)
