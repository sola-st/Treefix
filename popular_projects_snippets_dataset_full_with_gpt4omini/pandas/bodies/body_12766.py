# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
# GH 28256
result = ujson.encode(td, iso_dates=True)
expected = f'"{td.isoformat()}"'

assert result == expected
