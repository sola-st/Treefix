# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op = ops.Operation(ops._NodeDef("None", "myop"), ops.Graph(), [], [])
op._set_device("/job:goo/device:GPU:0")
self.assertProtoEquals(
    "op:'None' name:'myop' device:'/job:goo/device:GPU:0' ", op.node_def)
op = ops.Operation(ops._NodeDef("None", "op2"), ops.Graph(), [], [])
op._set_device(
    pydev.DeviceSpec(
        job="muu", device_type="CPU", device_index=0))
self.assertProtoEquals(
    "op:'None' name:'op2' device:'/job:muu/device:CPU:0'", op.node_def)
