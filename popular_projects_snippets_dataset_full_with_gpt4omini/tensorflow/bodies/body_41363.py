# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.device('/cpu:0'):
    v_cpu = resource_variable_ops.ResourceVariable([0.0, 1.0, 2.0],
                                                   name='cpu')
    v_also_cpu = resource_variable_ops.ResourceVariable([0.0, 1.0, 2.0],
                                                        name='also_cpu')

with ops.device('/gpu:0'):
    v_gpu = resource_variable_ops.ResourceVariable([0.0, 1.0, 2.0],
                                                   name='gpu')

@polymorphic_function.function
def resource_apply_adam():
    training_ops.resource_apply_adam(
        v_cpu.handle,
        v_gpu.handle,
        v_also_cpu.handle,
        1.0,  # beta1_power
        1.0,  # beta2_power
        1.0,  # learning_rate
        1.0,  # beta1
        1.0,  # beta2
        1.0,  # epsilon,
        [1.0, 1.0, 1.0],  # grad
        False)  # use_locking
    exit(None)

with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    'Cannot place the graph because a reference or resource edge connects '
    'colocation groups with incompatible assigned devices'):
    if not context.executing_eagerly():
        self.evaluate(variables.global_variables_initializer())
    self.evaluate(resource_apply_adam())
