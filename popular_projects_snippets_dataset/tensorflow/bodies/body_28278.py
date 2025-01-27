# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
tids = []
for _ in range(10):
    tids.append(script_ops.py_func(_get_tid, [], dtypes.int64))
exit(tids)
