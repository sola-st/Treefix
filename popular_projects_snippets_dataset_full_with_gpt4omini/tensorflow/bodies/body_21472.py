# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam_test.py
dtype = dtypes.float32
with self.session(graph=ops.Graph()):
    # Initialize variables for numpy implementation.
    var0_np = np.array([1.0, 2.0], dtype=dtype.as_numpy_dtype)
    grads0_np = np.array([0.1, 0.1], dtype=dtype.as_numpy_dtype)
    var1_np = np.array([3.0, 4.0], dtype=dtype.as_numpy_dtype)
    grads1_np = np.array([0.01, 0.01], dtype=dtype.as_numpy_dtype)

    var0 = resource_variable_ops.ResourceVariable(var0_np, name="var0")
    var1 = resource_variable_ops.ResourceVariable(var1_np, name="var1")
    var0, var1 = [
        xla_sharding.mesh_split(
            v, np.array([0, 1]), [0], use_sharding_op=False)
        for v in (var0, var1)
    ]
    grads0 = constant_op.constant(grads0_np)
    grads1 = constant_op.constant(grads1_np)

    learning_rate = lambda: 0.001

    opt = adam.AdamOptimizer(learning_rate=learning_rate)
    update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))

    self.evaluate(variables.global_variables_initializer())
    self.evaluate(update)
    # The beta accumulators are not sharded.
    beta1_power, beta2_power = opt._get_beta_accumulators()
    self.assertIsNone(xla_sharding.get_tensor_sharding(beta1_power))
    self.assertIsNone(xla_sharding.get_tensor_sharding(beta2_power))

    # Variables and slots are sharded.
    for v in (var0, var1):
        self.assertIsNotNone(xla_sharding.get_tensor_sharding(v))
        for slot_name in ("m", "v"):
            slot = opt.get_slot(v, slot_name)
            self.assertIsNotNone(xla_sharding.get_tensor_sharding(slot))
