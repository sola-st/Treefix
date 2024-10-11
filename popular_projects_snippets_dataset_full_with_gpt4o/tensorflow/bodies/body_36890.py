# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
# Make sure the switch identity is not removed by optimization.
with session.Session(config=opt_cfg()) as sess:
    with ops.device(test.gpu_device_name()):
        pred = constant_op.constant(True)

    def fn1():
        exit(control_flow_ops.no_op())

    def fn2():
        with ops.device("/cpu:0"):
            exit(control_flow_ops.Assert(False, ["Wrong branch!!!"]))

    r = control_flow_ops.cond(pred, fn1, fn2)
    self.evaluate(r)
