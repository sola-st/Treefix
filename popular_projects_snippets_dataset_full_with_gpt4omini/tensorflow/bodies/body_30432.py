# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/slice_op_test.py
# Tensor iteration is disabled explicitly for only graph mode.
with ops.Graph().as_default():
    # NOTE(mrry): If we register __getitem__ as an overloaded
    # operator, Python will valiantly attempt to iterate over the
    # Tensor from 0 to infinity.  This test ensures that this
    # unintended behavior is prevented.
    c = constant_op.constant(5.0)
    with self.assertRaisesRegex(errors_impl.OperatorNotAllowedInGraphError,
                                "Iterating over a symbolic `tf.Tensor`"):
        for _ in c:
            pass
