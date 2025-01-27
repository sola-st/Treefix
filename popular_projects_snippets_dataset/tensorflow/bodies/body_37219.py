# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with ops.Graph().as_default():
    # device set on tensor => same device on dep.
    with ops.device("/job:ps"):
        vd = variables.VariableV1([0.0])
    with_vd_dep = control_flow_ops.with_dependencies([vd.initializer], vd)
    self.assertTrue("/job:ps" in with_vd_dep.device)

    # No device set on tensor => no device on dep.
    vnod = variables.VariableV1([0.0])
    with_vnod_dep = control_flow_ops.with_dependencies([vnod.initializer],
                                                       vnod)
    self.assertDeviceEqual(None, with_vnod_dep.device)

    # device set on tensor, default device on graph => default device on dep.
    vdef = variables.VariableV1([0.0], name="vdef")
    with ops.device("/job:worker/device:GPU:1"):
        with_vdef_dep = control_flow_ops.with_dependencies([vdef.initializer],
                                                           vdef)
        # The device is empty, but the colocation constraint is set.
        self.assertDeviceEqual("", with_vdef_dep.device)
        self.assertEqual([b"loc:@vdef"], with_vdef_dep.op.colocation_groups())
