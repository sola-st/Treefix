# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
op1 = g.create_op("FloatOutput", [], [dtypes.float32], None, name="myop1")
with g.device("/device:GPU:0"):
    op2 = g.create_op(
        "FloatOutputStringOutput", [], [dtypes.float32, dtypes.string], None,
        name="myop2")
op3 = g.create_op(
    "Foo3",
    [list(op1.values())[0], list(op2.values())[1], list(op2.values())[0]],
    [dtypes.float32, dtypes.int32],
    None,
    name="myop3")
self.assertDeviceEqual(None, op1.device)
self.assertDeviceEqual("/device:GPU:0", op2.device)
self.assertDeviceEqual(None, op3.device)
self.assertProtoEquals("name:'myop1' op:'FloatOutput'", op1.node_def)
self.assertProtoEquals(
    "name:'myop2' op:'FloatOutputStringOutput' device:'/device:GPU:0'",
    op2.node_def)
self.assertProtoEquals(
    "name:'myop3' input:'myop1' input:'myop2:1' input:'myop2' op:'Foo3'",
    op3.node_def)
