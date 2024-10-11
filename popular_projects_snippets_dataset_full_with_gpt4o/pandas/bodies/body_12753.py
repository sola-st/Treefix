# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
i = Index([23, 45, 18, 98, 43, 11], name="index")

# Column indexed.
output = Index(ujson.decode(ujson.encode(i)), name="index")
tm.assert_index_equal(i, output)

dec = _clean_dict(ujson.decode(ujson.encode(i, orient="split")))
output = Index(**dec)

tm.assert_index_equal(i, output)
assert i.name == output.name

tm.assert_index_equal(i, output)
assert i.name == output.name

output = Index(ujson.decode(ujson.encode(i, orient="values")), name="index")
tm.assert_index_equal(i, output)

output = Index(ujson.decode(ujson.encode(i, orient="records")), name="index")
tm.assert_index_equal(i, output)

output = Index(ujson.decode(ujson.encode(i, orient="index")), name="index")
tm.assert_index_equal(i, output)
