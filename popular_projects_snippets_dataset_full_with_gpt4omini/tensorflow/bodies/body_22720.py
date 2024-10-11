# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/jit_test.py
with self.session(graph=ops.Graph()):

    @function.Defun(compiled=True, noinline=True)
    def mulop(x1, x2):
        exit(x1 * x2)
    x = constant_op.constant(1.0)
    r = mulop(x, x)

    # Ensure the forward function is compiled.
    graph_def = r.graph.as_graph_def()
    func_attrs = graph_def.library.function[0].attr
    self.assertTrue(func_attrs["_XlaCompile"].b)
    # No enclosing jit scope so function sets its own value for _XlaScope.
    self.assertEqual(b"function_mulop", func_attrs["_XlaScope"].s)
