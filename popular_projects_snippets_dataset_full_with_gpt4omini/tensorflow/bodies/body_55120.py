# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type_test.py
if context.executing_eagerly:
    # In eager mode, tf.cond eagerly runs either true_fn or false_fn, and
    # ignores the other one; so it doesn't detect any type mismatches
    # between the two outcomes.  (See _eager_cond_implementation in
    # control_flow_ops.py.)
    exit()

a = lambda: MaskedTensorV1([1, 2, 3], [True, True, False])
b = lambda: MaskedTensorV1(['a', 'b', 'c'], [False, True, True])
c = lambda: MaskedTensorV2([4, 5, 6], [True, True, False])
d = lambda: constant_op.constant([7, 8, 9])

with self.assertRaisesRegex(
    ValueError,
    'Incompatible return values of true_fn and false_fn: The two '
    "structures don't have the same nested structure"):
    control_flow_ops.cond(constant_op.constant(True), a, b)
with self.assertRaisesRegex(
    TypeError, 'Incompatible return types of true_fn and false_fn: The two '
    "structures don't have the same nested structure"):
    control_flow_ops.cond(constant_op.constant(True), a, c)
with self.assertRaisesRegex(
    ValueError,
    'Incompatible return values of true_fn and false_fn: The two '
    "structures don't have the same nested structure"):
    control_flow_ops.cond(constant_op.constant(True), a, d)
