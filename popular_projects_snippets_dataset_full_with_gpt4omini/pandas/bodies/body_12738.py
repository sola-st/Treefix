# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
klass = np.dtype(any_int_numpy_dtype).type
num = klass(1)

assert klass(ujson.decode(ujson.encode(num))) == num
