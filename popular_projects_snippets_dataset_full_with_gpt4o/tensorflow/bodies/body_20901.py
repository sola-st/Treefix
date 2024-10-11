# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum_test.py
optimizer = momentum_lib.MomentumOptimizer(0.01, 0.5)
with ops.Graph().as_default():
    var0 = resource_variable_ops.ResourceVariable([1.0, 2.0],
                                                  dtype=dtypes.float32,
                                                  name="var0")
    var1 = resource_variable_ops.ResourceVariable([3.0, 4.0],
                                                  dtype=dtypes.float32,
                                                  name="var1")
    loss = math_ops.reduce_sum(var0 + var1)
    optimizer.minimize(loss)
    optimizer_variables = optimizer.variables()
    self.assertStartsWith(optimizer_variables[0].name, "var0")
    self.assertStartsWith(optimizer_variables[1].name, "var1")
    self.assertEqual(2, len(optimizer_variables))

with ops.Graph().as_default():
    var2 = resource_variable_ops.ResourceVariable([1.0, 2.0],
                                                  dtype=dtypes.float32,
                                                  name="var2")
    var3 = resource_variable_ops.ResourceVariable([3.0, 4.0],
                                                  dtype=dtypes.float32,
                                                  name="var3")
    loss = math_ops.reduce_sum(var2 + var3)
    optimizer.minimize(loss)
    optimizer_variables = optimizer.variables()
    self.assertStartsWith(optimizer_variables[0].name, "var2")
    self.assertStartsWith(optimizer_variables[1].name, "var3")
    self.assertEqual(2, len(optimizer_variables))
