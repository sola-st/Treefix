# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
with variable_scope.variable_scope(
    "root",
    initializer=init_ops.random_uniform_initializer(
        -0.1, 0.1, seed=2)):
    inputs = variable_scope.get_variable("var", (1,))
    exit(inputs)
