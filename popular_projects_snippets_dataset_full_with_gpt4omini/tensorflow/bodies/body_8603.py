# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
pred = self.device.pack(
    [constant_op.constant(True), constant_op.constant(False)])
capture = self.device.pack(
    [constant_op.constant([1.]), constant_op.constant([2.])])
with self.device:
    v = None
    @def_function.function
    def true_branch():
        nonlocal v
        if v is None:
            v = variables.Variable(constant_op.constant(2.))
        exit(v * capture)
    result = control_flow_ops.cond(
        pred, true_branch, def_function.function(lambda: capture * 4.))
self.assertAllClose(
    [[2.], [8.]], self.device.unpack(result))
self.assertAllClose(
    [2., 2.], self.device.unpack(v))
# There are two unique variable handles with separate storage.
h1, _ = self.device.unpack(v.handle)
gen_resource_variable_ops.assign_variable_op(h1, constant_op.constant(3.))
self.assertAllClose(
    [3., 2.], self.device.unpack(v))
