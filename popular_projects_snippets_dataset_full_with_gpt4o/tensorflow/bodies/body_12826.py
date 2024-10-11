# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops_test.py
true_in, false_in = array_ops.constant(1.), array_ops.constant(5.)
with backprop.GradientTape(persistent=True) as tape:
    tape.watch(true_in)
    tape.watch(false_in)
    cond_true = control_flow_ops.cond(
        array_ops.constant(True), lambda: true_in**2., lambda: false_in**2.)
    cond_false = control_flow_ops.cond(
        array_ops.constant(False), lambda: true_in**2., lambda: false_in**2.)
grads_true = tape.gradient(
    cond_true, [true_in, false_in], output_gradients=3.)
grads_false = tape.gradient(
    cond_false, [true_in, false_in], output_gradients=3.)
self.assertEqual(3. * 2. * 1., self.evaluate(grads_true[0]))
self.assertEqual(None if context.executing_eagerly() else 0.,
                 self.evaluate(grads_true[1]))
self.assertEqual(3. * 2. * 5., self.evaluate(grads_false[1]))
self.assertEqual(None if context.executing_eagerly() else 0.,
                 self.evaluate(grads_false[0]))
