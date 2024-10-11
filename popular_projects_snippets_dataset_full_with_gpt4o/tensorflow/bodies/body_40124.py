# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
# Watching depends on nesting, not creation order
c = constant_op.constant(1.)
if forward_prop_first:
    forward_accumulator = forwardprop.ForwardAccumulator(c, .1)
    gradient_tape = backprop.GradientTape()
else:
    gradient_tape = backprop.GradientTape()
    forward_accumulator = forwardprop.ForwardAccumulator(c, .1)
try:
    gc.disable()
    with gradient_tape as tape:
        # Adding and removing the tape multiple times in different nesting
        # patterns does not affect watch ordering.
        pass
    with forward_accumulator as acc:
        with gradient_tape as tape:
            tape.watch(c)
            d = math_ops.cos(c)
            self.assertFalse(tape_lib.should_record_backprop((acc.jvp(d),)))
            e = math_ops.cos(acc.jvp(d))
            math_ops.cos(e)
            weak_e = weakref.ref(e)
            del e
            self.assertIsNone(weak_e())
        self.assertIsNone(tape.gradient(acc.jvp(d), c))
finally:
    gc.enable()
