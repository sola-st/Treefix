# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
x = constant_op.constant([1.3, 2])
with self.assertRaises(TypeError):
    int(x)
with self.assertRaises(TypeError):
    float(x)
