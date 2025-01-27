# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
op0 = g.create_op("TwoFloatOutputs", [], [dtypes.float32, dtypes.float32])
self.assertEqual("TwoFloatOutputs", op0.name)
self.assertEqual("TwoFloatOutputs:0", op0.outputs[0].name)
self.assertEqual("TwoFloatOutputs:1", op0.outputs[1].name)

op1 = g.create_op("FloatOutput", [], [dtypes.float32])
self.assertEqual("FloatOutput", op1.name)
self.assertEqual("FloatOutput:0", op1.outputs[0].name)

op2 = g.create_op("FloatOutput", [], [dtypes.float32])
self.assertEqual("FloatOutput_1", op2.name)
self.assertEqual("FloatOutput_1:0", op2.outputs[0].name)

op3 = g.create_op("FloatOutput", [], [dtypes.float32], name="my_op")
self.assertEqual("my_op", op3.name)
self.assertEqual("my_op:0", op3.outputs[0].name)
