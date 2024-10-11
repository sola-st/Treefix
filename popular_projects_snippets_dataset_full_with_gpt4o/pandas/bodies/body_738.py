# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
assert not is_scalar({})
assert not is_scalar([])
assert not is_scalar([1])
assert not is_scalar(())
assert not is_scalar((1,))
assert not is_scalar(slice(None))
assert not is_scalar(Ellipsis)
