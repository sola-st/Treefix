# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
klass = np.dtype(float_numpy_dtype).type
num = klass(256.2013)

assert klass(ujson.decode(ujson.encode(num))) == num
