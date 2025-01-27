# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
op1 = test_ops.float_output(name="myop1").op
self.assertEqual(1, len(op1.values()))
float1_t, = op1.values()

op2 = test_ops.float_output_string_output(name="myop2").a.op
self.assertEqual(2, len(op2.values()))
float2_t, label2_str_t = op2.values()

# Note that we consume label2_str_t twice here.
op3 = test_ops.foo2(float1_t, label2_str_t, label2_str_t, name="myop3").d.op
self.assertEqual(2, len(op3.values()))

self.assertEqual(1, len(float1_t.consumers()))
self.assertEqual(op3, float1_t.consumers()[0])

self.assertEqual(0, len(float2_t.consumers()))

self.assertEqual(2, len(label2_str_t.consumers()))
self.assertEqual(op3, label2_str_t.consumers()[0])
self.assertEqual(op3, label2_str_t.consumers()[1])

self.assertProtoEquals("""
    op:'Foo2' name:'myop3'
    input:'myop1' input:'myop2:1' input:'myop2:1'
    """, op3.node_def)
