# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame({"foobar": 1}, index=range(10))

df.foobar = 5
assert (df.foobar == 5).all()
