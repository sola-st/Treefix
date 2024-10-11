# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py
x = constant_op.constant(1.)
tangents = random_ops.random_normal(shape=[10], seed=1)
expected = [-t * math_ops.cos(1.) for t in tangents]
if forward_prop_first:
    batch_acc = forwardprop.ForwardAccumulator._batch_accumulator(x, tangents)
    gradient_tape = backprop.GradientTape(persistent=True)
else:
    gradient_tape = backprop.GradientTape(persistent=True)
    batch_acc = forwardprop.ForwardAccumulator._batch_accumulator(x, tangents)
with gradient_tape as tape:
    with batch_acc as acc:
        tape.watch(x)
        y = math_ops.cos(x)
        self.assertTrue(tape_lib.should_record_backprop((acc.jvp(y),)))
        jvps = acc.jvp(y)
    d2y_dx2 = [tape.gradient(dy_dx, x) for dy_dx in jvps]
self.assertAllClose(expected, d2y_dx2)
