# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_ops_test.py
with test_util.use_gpu():
    # The variable and an op to increment it are on the GPU.
    var = state_ops.variable_op([1], dtypes.float32)
    self.evaluate(state_ops.assign(var, [1.0]))
    increment = state_ops.assign_add(var, [1.0])
    with ops.control_dependencies([increment]):
        with test_util.force_cpu():
            # This mul op is pinned to the CPU, but reads the variable from the
            # GPU. The test ensures that the dependency on 'increment' is still
            # honored, i.e., the Send and Recv from GPU to CPU should take place
            # only after the increment.
            result = math_ops.multiply(var, var)
    self.assertAllClose([4.0], self.evaluate(result))
