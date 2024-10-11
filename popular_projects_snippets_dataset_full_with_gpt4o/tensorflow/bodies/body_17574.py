# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
shape = (5, 6, 4)
with self.cached_session():
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        self._runner(
            init_ops.Constant(2),
            tensor_shape,
            target_mean=2,
            target_max=2,
            target_min=2)
