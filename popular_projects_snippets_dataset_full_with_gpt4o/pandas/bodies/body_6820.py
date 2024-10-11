# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# GH 19262: conversion via dtype parameter
expected_kwargs = self.get_kwargs_from_breaks(breaks.astype(subtype))
expected = constructor(**expected_kwargs)

result_kwargs = self.get_kwargs_from_breaks(breaks)
iv_dtype = IntervalDtype(subtype, "right")
for dtype in (iv_dtype, str(iv_dtype)):
    result = constructor(dtype=dtype, **result_kwargs)
    tm.assert_index_equal(result, expected)
