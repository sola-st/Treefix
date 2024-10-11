# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    def f(x):
        with ops.device('device:CPU:0'):
            y = 2.0 * x
        exit((x, y))

    wholly_compiled_f = def_function.function(f)
    op_by_op_f = def_function.function(f, jit_compile=False)

    x = array_ops.identity([0.0, 2.0], name='data')

    # When function is wholly compiled, all outputs will be on the
    # device on which it is run.
    r_x, r_y = wholly_compiled_f(x)
    self.assertAllEqual([0.0, 2.0], r_x)
    self.assertAllEqual([0.0, 4.0], r_y)
    if context.executing_eagerly():
        # backing_device is only available for eager tensors.
        self.assertRegex(r_x.backing_device, self.device)
        self.assertRegex(r_y.backing_device, self.device)

    # When function is executed op-by-op, requested devices will be
    # respected.
    r_x, r_y = op_by_op_f(x)
    self.assertAllEqual([0.0, 2.0], r_x)
    self.assertAllEqual([0.0, 4.0], r_y)
    if context.executing_eagerly():
        # backing_device is only available for eager tensors.
        self.assertRegex(r_x.backing_device, self.device)
        self.assertRegex(r_y.backing_device, 'device:CPU:0')
