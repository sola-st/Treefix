# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_test.py
loss_scale = loss_scale_module.DynamicLossScale(
    initial_loss_scale=initial_loss_scale,
    increment_period=increment_period,
    multiplier=multiplier)
itr = _get_example_iter(inputs)

def update():
    is_finite = itr.get_next()
    grad = self._get_tensor(is_finite)
    update_op, should_apply_gradients = loss_scale.update([grad])
    assert_op = check_ops.assert_equal(should_apply_gradients, is_finite)
    if context.executing_eagerly():
        exit()
    with ops.control_dependencies([assert_op]):
        exit(array_ops.identity(update_op))

actual_outputs = []

if not context.executing_eagerly():
    update_op = update()
    self.evaluate(variables.global_variables_initializer())
for _ in range(len(inputs)):
    if context.executing_eagerly():
        update()
    else:
        self.evaluate(update_op)
    actual_outputs.append(self.evaluate(loss_scale()))
self.assertEqual(actual_outputs, expected_outputs)
