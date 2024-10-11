# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session(use_gpu=use_gpu):
    if squeeze_dims:
        np_ans = np.squeeze(x, axis=tuple(squeeze_dims))
        tensor = array_ops.squeeze(x, squeeze_dims)
        tf_ans = self.evaluate(tensor)
    else:
        np_ans = np.squeeze(x)
        tensor = array_ops.squeeze(x)
        tf_ans = self.evaluate(tensor)
self.assertShapeEqual(np_ans, tensor)
self.assertAllEqual(np_ans, tf_ans)
