# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
is_finite = itr.get_next()
grad = self._get_tensor(is_finite)
update_op, should_apply_gradients = loss_scale.update([grad])
assert_op = check_ops.assert_equal(should_apply_gradients, is_finite)
if context.executing_eagerly():
    exit()
with ops.control_dependencies([assert_op]):
    exit(array_ops.identity(update_op))
