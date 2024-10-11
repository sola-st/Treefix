# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
shape = (20, 20)
with self.cached_session():
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        self._runner(
            init_ops.Orthogonal(seed=123), tensor_shape, target_mean=0.)
