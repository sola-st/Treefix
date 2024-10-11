# Extracted from ./data/repos/pandas/pandas/tests/tseries/frequencies/test_freq_code.py
# see gh-14378
off = to_offset(str(args[0]) + args[1])
assert off.n == expected[0]
assert off._prefix == expected[1]
