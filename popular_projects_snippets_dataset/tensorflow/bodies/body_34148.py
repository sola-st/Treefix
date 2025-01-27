# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
# GPU kernels don't throw exceptions.
with self.cached_session(use_gpu=False) as sess:
    shape = (2, 3)
    indices = array_ops.placeholder(shape=shape, dtype=np.int32)
    data = np.zeros(shape + (5,))
    partitions = data_flow_ops.dynamic_partition(
        data, indices, num_partitions=7)
    for i in range(2):
        for j in range(3):
            bad = np.zeros(shape, dtype=np.int32)
            bad[i, j] = 17
            with self.assertRaisesOpError(
                r"partitions\[%d,%d\] = 17 is not in \[0, 7\)" % (i, j)):
                sess.run(partitions, feed_dict={indices: bad})
