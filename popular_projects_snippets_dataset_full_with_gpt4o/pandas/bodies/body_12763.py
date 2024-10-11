# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
s = set()

for x in range(0, 100000):
    s.add(x)

# Make sure no Exception is raised.
ujson.encode(s)
