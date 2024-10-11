# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
if shape is None:
    shape = [0]
exit((np.empty(shape=(0, len(shape)), dtype=np.int64),
        np.array([], dtype=dtype), np.array(shape, dtype=np.int64)))
