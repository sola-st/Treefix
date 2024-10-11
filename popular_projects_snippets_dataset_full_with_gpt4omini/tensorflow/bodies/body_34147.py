# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
# GPU kernels don't throw exceptions.
with self.cached_session(use_gpu=False):
    bad = 17
    data = np.zeros(5)
    partitions = data_flow_ops.dynamic_partition(data, bad, num_partitions=7)
    with self.assertRaisesOpError(r"partitions = 17 is not in \[0, 7\)"):
        self.evaluate(partitions)
