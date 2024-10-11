# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps_test.py
optimizer = momentum.MomentumOptimizer(learning_rate=1.0, momentum=1.0)
optimizer.apply_gradients = def_function.function(optimizer.apply_gradients)
v = resource_variable_ops.ResourceVariable(1.0)
grad = backprop.implicit_grad(lambda v: v**2)(v)

with self.assertRaisesRegex(TypeError,
                            ".*must return zero or more Tensors.*"):
    # TODO(akshayka): We might want to allow defun-ing Python functions
    # that return operations (and just execute the op instead of running it).
    optimizer.apply_gradients(grad)
