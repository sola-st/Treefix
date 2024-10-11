# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/conditional_accumulator_test.py
with self.cached_session():
    q = data_flow_ops.ConditionalAccumulator(
        dtypes_lib.float32, name="Q", shape=tensor_shape.TensorShape([1]))

    global_step = variables.Variable(0, name="global_step")
    new_global_step = math_ops.add(global_step, 1)
    inc_global_step = state_ops.assign(global_step, new_global_step)

    set_global_step_op = q.set_global_step(new_global_step)

    self.evaluate(variables.global_variables_initializer())
    for _ in range(3):
        set_global_step_op.run()
        self.evaluate(inc_global_step)
