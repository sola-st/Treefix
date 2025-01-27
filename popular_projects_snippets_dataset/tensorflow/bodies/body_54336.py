# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
t1 = _apply_op(g, "FloatOutput", [], [dtypes.float32], name="myop1")
with g.device("/device:GPU:0"):
    t2 = _apply_op(
        g, "TwoIntOutputs", [], [dtypes.int32, dtypes.int32], name="myop2")
t3 = _apply_op(
    g,
    "Foo1", [t1, t2[1], t2[0]], [dtypes.float32, dtypes.int32],
    name="myop3")
self.assertTrue(isinstance(t1, ops.Tensor))
self.assertTrue(isinstance(t2, list))
self.assertTrue(isinstance(t3, list))
self.assertTrue(isinstance(t3[0], ops.Tensor))
self.assertEqual("myop1", t1._as_node_def_input())
self.assertEqual("myop2", t2[0]._as_node_def_input())
self.assertEqual("myop2:1", t2[1]._as_node_def_input())
self.assertEqual("myop3", t3[0]._as_node_def_input())
# Validate that we got the right ops as well
self.assertProtoEquals("name:'myop1' op:'FloatOutput'", t1.op.node_def)
self.assertProtoEquals(
    "name:'myop2' op:'TwoIntOutputs' device:'/device:GPU:0'",
    t2[0].op.node_def)
self.assertProtoEquals(
    "name:'myop3' input:'myop1' input:'myop2:1' input:'myop2' op:'Foo1'",
    t3[0].op.node_def)
