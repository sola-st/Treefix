# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
shape = (12, 99, 7)
with self.cached_session():
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        self._runner(
            init_ops.TruncatedNormal(mean=0, stddev=1, seed=126),
            tensor_shape,
            target_mean=0.,
            target_max=2,
            target_min=-2)
