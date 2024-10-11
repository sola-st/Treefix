# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
with self.cached_session():
    shape = (3, 4, 5)
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        with self.assertRaises(ValueError):
            self._runner(
                init_ops.Identity(),
                tensor_shape,
                target_mean=1. / int(tensor_shape[0]),
                target_max=1.)

    shape = (3, 3)
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        self._runner(
            init_ops.Identity(),
            tensor_shape,
            target_mean=1. / int(tensor_shape[0]),
            target_max=1.)
