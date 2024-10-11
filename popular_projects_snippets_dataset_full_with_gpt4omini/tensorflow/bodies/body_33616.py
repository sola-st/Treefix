# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
if not shape:
    shape = (1, len(values))
dtype = queue.dtypes[0]
sess.run(
    queue.enqueue(constant_op.constant(
        values, dtype=dtype, shape=shape)))
