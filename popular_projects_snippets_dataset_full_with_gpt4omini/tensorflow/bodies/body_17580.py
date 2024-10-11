# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
shape = (5, 6, 4, 2)
with self.cached_session():
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        fan_in, _ = init_ops._compute_fans(tensor_shape)
        std = np.sqrt(2. / fan_in)
        self._runner(
            init_ops.he_normal(seed=123),
            tensor_shape,
            target_mean=0.,
            target_std=std)
