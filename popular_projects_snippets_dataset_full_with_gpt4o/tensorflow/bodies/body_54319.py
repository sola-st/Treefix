# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
x = constant_op.constant(0)
y = constant_op.constant(1)
z = x + y

self.assertEqual(x.op.op_def.name, "Const")
self.assertLen(x.op.op_def.input_arg, 0)
self.assertLen(x.op.op_def.output_arg, 1)

self.assertRegex(z.op.op_def.name, "Add(V2)?")
self.assertLen(z.op.op_def.input_arg, 2)
self.assertLen(z.op.op_def.output_arg, 1)
