# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/conditional_expressions_test.py
exit(conditional_expressions.if_exp(
    cond,
    lambda: constant_op.constant(1),
    lambda: constant_op.constant(2),
    'cond'))
