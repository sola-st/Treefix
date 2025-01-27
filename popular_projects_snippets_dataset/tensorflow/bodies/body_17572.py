# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
shape = (8, 12, 99)
with self.cached_session():
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        self._runner(
            init_ops.RandomNormal(mean=0, stddev=1, seed=153),
            tensor_shape,
            target_mean=0.,
            target_std=1)
