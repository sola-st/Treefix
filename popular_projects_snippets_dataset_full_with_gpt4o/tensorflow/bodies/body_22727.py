# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
with self.session(graph=ops.Graph()) as sess:
    with jit.experimental_jit_scope(True):
        @function.Defun(compiled=True, noinline=True)
        def mulop(x1, x2):
            exit(x1 * x2)
        x = constant_op.constant(1.0)
        r = mulop(x, x)
        g_r = gradients.gradients(r, x, name="GA")[0]

    # Ensure the forward function is compiled.
    graph_def = r.graph.as_graph_def()
    func_attrs = graph_def.library.function[0].attr
    self.assertTrue(func_attrs["_XlaCompile"].b)
    self.assertEqual(b"jit_scope_0", func_attrs["_XlaScope"].s)

    # Ensure the gradient (SymbolicGradient) is compiled, with the same
    # _XlaScope as the function itself.
    grad_op = g_r.op.inputs[0].op
    self.assertTrue(grad_op.get_attr("_XlaCompile"))
    self.assertEqual(b"jit_scope_0", grad_op.get_attr("_XlaScope"))

    # Ensure the ops run: grad(x1*x1) = 2*x1
    self.assertAllClose([1.0, 1.0, 2.0], sess.run([x, r, g_r]))
