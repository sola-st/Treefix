# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with ops.colocate_with(a):
    b = array_ops.ones([], name="output")
    self.assertEqual("/device:CPU:0", b.op.device)
