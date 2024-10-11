# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
num = 1e-40
assert num == ujson.decode(ujson.encode(num))
num = 1e-100
assert num == ujson.decode(ujson.encode(num))
num = -1e-45
assert num == ujson.decode(ujson.encode(num))
num = -1e-145
assert np.allclose(num, ujson.decode(ujson.encode(num)))
