# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
g = ops.Graph()
with g.as_default():
    x = test_ops.int_output()
    op = test_ops.int_input_int_output(x, name="myop").op
with self.assertRaisesRegex(AttributeError,
                            "'tuple' object has no attribute 'append'"):
    op.inputs.append(None)
