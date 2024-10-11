# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    inp = constant(1.0, shape=[32, 100], name="in")
    w = constant(1.0, shape=[100, 10], name="w")
    b = constant(1.0, shape=[10], name="b")
    xw = math_ops.matmul(inp, w, name="xw")
    h = bias_add(xw, b, name="h")
    w_grad = gradients.gradients(h, w)[0]
self.assertEqual("MatMul", w_grad.op.type)
self.assertEqual(w_grad.op._original_op, xw.op)
self.assertTrue(w_grad.op.get_attr("transpose_a"))
self.assertFalse(w_grad.op.get_attr("transpose_b"))
