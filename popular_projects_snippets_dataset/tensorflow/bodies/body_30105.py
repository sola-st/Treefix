# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
for index in ("ij", "xy"):
    numpy_out = np.meshgrid(x, y, indexing=index)
    tf_out = array_ops.meshgrid(x, y, indexing=index)
    with self.cached_session(use_gpu=use_gpu):
        for xx, yy in zip(numpy_out, tf_out):
            self.assertAllEqual(xx, yy)
