# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/op_def_library_test.py
with ops.Graph().as_default():
    a = op_def_library.apply_op("Simple", a=3)
with ops.Graph().as_default():
    b = op_def_library.apply_op("Simple", a=4)
with self.assertRaises(ValueError) as cm:
    op_def_library.apply_op("Binary", a=a, b=b)
self.assertIn("must be from the same graph", str(cm.exception))
