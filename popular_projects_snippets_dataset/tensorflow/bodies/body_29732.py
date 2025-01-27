# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_gather_op_test.py
with ops.device_v2("cpu:0"):
    params = [[0, 1, 2], [3, 4, 5]]
    with self.assertRaisesOpError(r"indices\[0\] = 7 is not in \[0, 2\)"):
        self.evaluate(array_ops.batch_gather(params, [7]))
