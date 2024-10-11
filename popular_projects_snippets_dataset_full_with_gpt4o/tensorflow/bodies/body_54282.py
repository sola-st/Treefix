# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op = test_ops.float_output_string_output(name="myop").a.op
self.assertEqual(2, len(op.values()))
self.assertEqual(0, len(op.inputs))
self.assertEqual("myop", op.name)

float_t, label_str_t = op.values()
self.assertEqual(dtypes.float32, float_t.dtype)
self.assertEqual(op, float_t.op)
self.assertEqual(0, float_t._value_index)
self.assertEqual(0, len(float_t.consumers()))
self.assertEqual("myop", float_t._as_node_def_input())

self.assertEqual(dtypes.string, label_str_t.dtype)
self.assertEqual(op, label_str_t.op)
self.assertEqual(1, label_str_t._value_index)
self.assertEqual(0, len(label_str_t.consumers()))
self.assertEqual("myop:1", label_str_t._as_node_def_input())

self.assertProtoEquals("op:'FloatOutputStringOutput' name:'myop'",
                       op.node_def)
