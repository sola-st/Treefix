# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
shape = (4, 5)
with self.cached_session():
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        self._runner(
            init_ops.Ones(), tensor_shape, target_mean=1., target_max=1.)
