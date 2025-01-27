# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
for _ in range(1000):
    with pytest.raises(ValueError, match=re.escape(err_msg)):
        ujson.decode(broken_json)
