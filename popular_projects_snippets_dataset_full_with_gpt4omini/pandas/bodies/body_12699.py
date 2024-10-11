# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
# see gh-11473: to_json segfaults with timezone-aware datetimes
test = datetime.time(10, 12, 15, 343243, pytz.utc)
output = ujson.encode(test)
expected = f'"{test.isoformat()}"'
assert expected == output
