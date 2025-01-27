# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
with self.cached_session():
    indices = []
    np_values = []
    values = []
    for _ in range(10):
        indices.extend([ops.convert_to_tensor(np.arange(100).astype(np.int32))])
        np_values.extend([np.random.uniform(size=100)])
        values.extend([ops.convert_to_tensor(np_values[-1])])
    stitched = data_flow_ops.dynamic_stitch(indices, values)
self.assertAllEqual(np_values[-1], stitched)
