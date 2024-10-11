# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
"""Test that the stateful initializer is not marked for compilation.

    XLA does not currently support seeded initialization and XLA initializers
    therefore return different values than non-XLA counterparts.  Here
    we ensure that if we can disable JIT compilation for the initializers and
    get the same variable values as if no JIT compilation happened.
    """
def create_ops():
    with variable_scope.variable_scope(
        "root",
        initializer=init_ops.random_uniform_initializer(
            -0.1, 0.1, seed=2)):
        inputs = variable_scope.get_variable("var", (1,))
        exit(inputs)
_, v_false_1 = self.compute(False, create_ops)
_, v_false_2 = self.compute(False, create_ops)
_, v_true_1 = self.compute(enable_jit_nonstateful, create_ops)
_, v_true_2 = self.compute(enable_jit_nonstateful, create_ops)
self.assertAllClose(v_false_1, v_false_2)
self.assertAllClose(v_true_1, v_true_2)
self.assertAllClose(v_false_1, v_true_1)
