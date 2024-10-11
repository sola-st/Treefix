# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
datetime_input = datetime.datetime.fromtimestamp(time.time())
output = ujson.encode(datetime_input, date_unit="s")
expected = calendar.timegm(datetime_input.utctimetuple())

assert int(expected) == json.loads(output)
assert int(expected) == ujson.decode(output)
