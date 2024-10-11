# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op1 = test_ops.float_output(name="myop1").op
float_t, = op1.values()
op2 = test_ops.float_input(float_t, name="myop2")
self.assertEqual(0, len(op2.values()))
self.assertEqual(1, len(op2.inputs))
self.assertIs(float_t, op2.inputs[0])

self.assertEqual(1, len(float_t.consumers()))
self.assertEqual(op2, float_t.consumers()[0])

self.assertProtoEquals("op:'FloatOutput' name:'myop1'", op1.node_def)
self.assertProtoEquals("op:'FloatInput' name:'myop2' input:'myop1'",
                       op2.node_def)
