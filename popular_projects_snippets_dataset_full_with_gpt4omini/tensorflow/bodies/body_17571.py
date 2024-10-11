# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
shape = (9, 6, 99)
with self.cached_session():
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        self._runner(
            init_ops.RandomUniform(minval=-1, maxval=1, seed=124),
            tensor_shape,
            target_mean=0.,
            target_max=1,
            target_min=-1)
