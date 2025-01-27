# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
np_ans = np.expand_dims(x, axis=dim)
with self.cached_session(use_gpu=use_gpu):
    tensor = array_ops.expand_dims(x, dim)
    tf_ans = self.evaluate(tensor)
self.assertShapeEqual(np_ans, tensor)
self.assertAllEqual(np_ans, tf_ans)
