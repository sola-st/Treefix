# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
# Make sure no Exception is raised.
for _ in range(10):
    base = "\u00e5".encode()
    escape_input = base * 1024 * 1024 * 2
    ujson.encode(escape_input)
