# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
# Make sure no Exception is raised.
for _ in range(10):
    base = "\u00e5".encode()
    quote = b'"'

    escape_input = quote + (base * 1024 * 1024 * 2) + quote
    ujson.decode(escape_input)
