# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/conditional_expressions_test.py
# tf.function required because eager cond degenerates to Python if.
@def_function.function
def test_fn():
    conditional_expressions.if_exp(
        constant_op.constant(True), lambda: 1.0, lambda: 2, 'expr_repr')

with self.assertRaisesRegex(
    TypeError,
    "'expr_repr' has dtype float32 in the main.*int32 in the else"):
    test_fn()
