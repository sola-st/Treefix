# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
c = constant_op.constant(1.)
# Watching depends on nesting, not creation order
if forward_prop_first:
    forward_accumulator = forwardprop.ForwardAccumulator(c, .1)
    gradient_tape = backprop.GradientTape()
else:
    gradient_tape = backprop.GradientTape()
    forward_accumulator = forwardprop.ForwardAccumulator(c, .1)
with gradient_tape as tape:
    with forward_accumulator as acc:
        tape.watch(c)
        d = math_ops.cos(c)
        self.assertTrue(tape_lib.should_record_backprop((acc.jvp(d),)))
    self.assertAllClose(-.1 * math_ops.cos(1.), tape.gradient(acc.jvp(d), c))
