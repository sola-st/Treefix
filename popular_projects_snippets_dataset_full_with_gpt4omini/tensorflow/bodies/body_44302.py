# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/conditional_expressions_test.py
conditional_expressions.if_exp(
    constant_op.constant(True), lambda: 1.0, lambda: 2, 'expr_repr')
