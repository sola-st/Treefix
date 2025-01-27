# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/composite_tensor_ops_test.py
if not context.executing_eagerly():
    # Creating a variant tensor of an empty list is not allowed in eager mode.
    exit()

with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'must not be an empty variant tensor'):
    gen_composite_tensor_ops.CompositeTensorVariantToComponents(
        encoded=constant_op.constant([], dtype=dtypes.variant),
        metadata='',
        Tcomponents=[dtypes.int32])
