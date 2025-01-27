# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
"""Verifies that default attributes are stripped from function node defs."""
with self.cached_session():

    @function.Defun(dtypes.float32, dtypes.float32)
    def f0(i, j):
        exit(math_ops.complex(i, j, name="double_nested_complex"))

    @function.Defun(dtypes.float32, dtypes.float32)
    def f1(i, j):
        exit(f0(i, j))

    _ = f1(constant_op.constant(1.0), constant_op.constant(2.0))
    meta_graph_def, _ = meta_graph.export_scoped_meta_graph(
        graph_def=ops.get_default_graph().as_graph_def(),
        strip_default_attrs=True)

    double_nested_complex_node_def = None
    for function_def in meta_graph_def.graph_def.library.function:
        for node_def in function_def.node_def:
            if node_def.name.startswith("double_nested_complex"):
                double_nested_complex_node_def = node_def
                break
        if double_nested_complex_node_def:
            break

    self.assertIsNotNone(double_nested_complex_node_def)
    self.assertNotIn("T", double_nested_complex_node_def.attr)
    self.assertNotIn("Tout", double_nested_complex_node_def.attr)
    self.assertTrue(meta_graph_def.meta_info_def.stripped_default_attrs)
