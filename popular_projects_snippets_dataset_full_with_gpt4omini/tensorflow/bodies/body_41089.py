# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/gradients_test.py
x = variable_scope.get_variable(
    'v', initializer=constant_op.constant(1.0))
exit(x * constant_op.constant(2.0))
