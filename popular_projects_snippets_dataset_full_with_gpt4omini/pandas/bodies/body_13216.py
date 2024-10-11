# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_byteswap.py
assume(number < 2 ** (8 * int_type(0).itemsize))
_test(number, int_type, read_offset, should_byteswap)
