# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
if dtype in (np.int8, np.uint8):
    N = 53
else:
    N = 11111
values = np.repeat(np.arange(N).astype(dtype), 5)
values[0] = 42
values.flags.writeable = writable
result = ht.mode(values, False)
assert result == 42
