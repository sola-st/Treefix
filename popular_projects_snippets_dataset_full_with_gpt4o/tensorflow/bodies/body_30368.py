# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
with test_util.force_cpu():
    params = [[0, 1, 2], [3, 4, 5]]
    with self.assertRaisesOpError(r"indices\[0,0\] = 7 is not in \[0, 2\)"):
        self.evaluate(array_ops.gather(params, [[7]], axis=0))
    with self.assertRaisesOpError(r"indices\[0,0\] = 7 is not in \[0, 3\)"):
        self.evaluate(array_ops.gather(params, [[7]], axis=1))
