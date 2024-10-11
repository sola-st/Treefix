# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
if any_int_numpy_dtype in ("int64", "uint64") and not IS64:
    pytest.skip("Cannot test 64-bit integer on 32-bit platform")

klass = np.dtype(any_int_numpy_dtype).type

# uint64 max will always overflow,
# as it's encoded to signed.
if any_int_numpy_dtype == "uint64":
    num = np.iinfo("int64").max
else:
    num = np.iinfo(any_int_numpy_dtype).max

assert klass(ujson.decode(ujson.encode(num))) == num
