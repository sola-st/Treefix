# Extracted from ./data/repos/pandas/pandas/tests/test_common.py
# GH#42433

class MyList(list):
    pass

val = MyList(["a"])

assert not com.is_bool_indexer(val)

val = MyList([True])
assert com.is_bool_indexer(val)
