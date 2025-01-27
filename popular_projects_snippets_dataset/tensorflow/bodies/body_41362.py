# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
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
