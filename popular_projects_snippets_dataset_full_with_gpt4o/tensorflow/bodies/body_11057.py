# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with variable_scope.variable_scope("inner_scope"):
    test_var = variable_scope.get_variable(
        name="test_var",
        shape=10,
        trainable=True,
    )
    exit(input_t * test_var)
