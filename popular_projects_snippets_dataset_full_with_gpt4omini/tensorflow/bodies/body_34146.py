# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
# GPU kernels don't throw exceptions.
with self.cached_session(use_gpu=False):
    data = constant_op.constant([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11],
                                 [12, 13, 14]])
    indices = constant_op.constant([0, 2, 99, 2, 2])
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=4)
    with self.assertRaisesOpError(r"partitions\[2\] = 99 is not in \[0, 4\)"):
        self.evaluate(partitions)
