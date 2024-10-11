# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_floats.py
# contains
# integer index
index = index_func(5)
obj = gen_obj(frame_or_series, index)

# coerce to equal int
assert 3.0 in obj
