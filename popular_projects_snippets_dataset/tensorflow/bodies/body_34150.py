# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/dynamic_partition_op_test.py
x = constant_op.constant(np.random.randn(3072))
inds = [0] * 189 + [1] * 184 + [2] * 184 + [3] * 191 + [4] * 192 + [
    5
] * 195 + [6] * 195
inds += [7] * 195 + [8] * 188 + [9] * 195 + [10] * 188 + [11] * 202 + [
    12
] * 194
inds += [13] * 194 + [14] * 194 + [15] * 192
self.assertEqual(len(inds), x.shape[0])
partitioned = data_flow_ops.dynamic_partition(x, inds, 16)
with self.cached_session():
    res = self.evaluate(partitioned)
self.assertEqual(res[-1].shape[0], 192)
