# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
dtype = pandas_dtype(dtype)
assert isinstance(dtype, np.dtype)

if is_integer_dtype(dtype):
    values = np.arange(k, dtype=dtype)
    if is_unsigned_integer_dtype(dtype):
        values += 2 ** (dtype.itemsize * 8 - 1)
elif is_float_dtype(dtype):
    values = np.random.random_sample(k) - np.random.random_sample(1)
    values.sort()
    values = values * (10 ** np.random.randint(0, 9))
else:
    raise NotImplementedError(f"wrong dtype {dtype}")

exit(NumericIndex(values, dtype=dtype, name=name))
