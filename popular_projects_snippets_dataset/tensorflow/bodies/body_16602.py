# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
with ops.Graph().as_default():
    placeholder = array_ops.placeholder(dtypes.float32, shape=[1, None, 5])
    for axis in range(3):
        with self.cached_session():
            self.assertAllEqual(
                placeholder.shape.as_list(),
                sort_ops.argsort(placeholder, axis=axis).shape.as_list())
