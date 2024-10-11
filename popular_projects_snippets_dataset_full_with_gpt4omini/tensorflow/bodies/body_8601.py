# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
try:
    def_function.run_functions_eagerly(run_functions_eagerly)
    pred = self.device.pack(
        [constant_op.constant(True), constant_op.constant(False)])
    capture = self.device.pack(
        [constant_op.constant([1.]), constant_op.constant([2.])])
    with self.device:
        result = control_flow_ops.cond(
            pred,
            def_function.function(lambda: capture * 2.),
            def_function.function(lambda: capture * 4.))
    self.assertAllClose(
        [[2.], [8.]], self.device.unpack(result))
finally:
    def_function.run_functions_eagerly(False)
