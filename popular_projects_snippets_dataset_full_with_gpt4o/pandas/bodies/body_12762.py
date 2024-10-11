# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
float_number *= sign
tm.assert_almost_equal(float_number, ujson.loads(str(float_number)), rtol=1e-15)
