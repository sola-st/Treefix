# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
with self.session(graph=ops.Graph()):
    with jit.experimental_jit_scope():
        # XlaScope 0
        a1 = constant_op.constant([[1.]])
        a1t = math_ops.matmul(a1, a1)
    with jit.experimental_jit_scope():
        # XlaScope 1
        a2 = constant_op.constant([[1.]])
        a2t = math_ops.matmul(a2, a2)

    self.assertEqual(b"jit_scope_0", a1.op.get_attr("_XlaScope"))
    self.assertEqual(b"jit_scope_1", a2.op.get_attr("_XlaScope"))
    grad_a1 = gradients.gradients(a1t, a1, name="GA")[0]
    grad_a2 = gradients.gradients(a2t, a2, name="GB")[0]
    grad_a1 = grad_a1.op.inputs[0]
    grad_a2 = grad_a2.op.inputs[0]
    self.assertTrue(grad_a1.op.get_attr("_XlaCompile"))
    self.assertTrue(grad_a2.op.get_attr("_XlaCompile"))
    self.assertEqual(b"jit_scope_0", grad_a1.op.get_attr("_XlaScope"))
    self.assertEqual(b"jit_scope_1", grad_a2.op.get_attr("_XlaScope"))
