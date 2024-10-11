# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
y = constant_op.constant(2.)
x = constant_op.constant(1.)
with backprop.GradientTape() as g:
    g.watch(x)
    tape_lib.record_operation('InvalidBackprop', [y], [x], lambda dy: [])
with self.assertRaisesRegex(errors_impl.InternalError,
                            'InvalidBackprop.*too few gradients'):
    g.gradient(y, x)
