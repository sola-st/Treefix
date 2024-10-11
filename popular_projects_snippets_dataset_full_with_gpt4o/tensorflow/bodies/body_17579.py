# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_test.py
shape = (5, 6, 4, 2)
with self.cached_session():
    for tensor_shape in [shape, tensor_shape_lib.TensorShape(shape)]:
        fan_in, fan_out = init_ops._compute_fans(tensor_shape)
        std = np.sqrt(2. / (fan_in + fan_out))
        self._runner(
            init_ops.glorot_normal_initializer(seed=123),
            tensor_shape,
            target_mean=0.,
            target_std=std)
