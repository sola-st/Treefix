# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
"""Verifies that default attributes are stripped from a graph def."""

# Complex Op has 2 attributes with defaults:
#   o "T"    : float32.
#   o "Tout" : complex64.

# When inputs to the Complex Op are float32 instances, "T" maps to float32
# and "Tout" maps to complex64. Since these attr values map to their
# defaults, they must be stripped unless stripping of default attrs is
# disabled.
with self.cached_session():
    real_num = constant_op.constant(1.0, dtype=dtypes.float32, name="real")
    imag_num = constant_op.constant(2.0, dtype=dtypes.float32, name="imag")
    math_ops.complex(real_num, imag_num, name="complex")

    # strip_default_attrs is enabled.
    meta_graph_def, _ = meta_graph.export_scoped_meta_graph(
        graph_def=ops.get_default_graph().as_graph_def(),
        strip_default_attrs=True)
    node_def = test_util.get_node_def_from_graph("complex",
                                                 meta_graph_def.graph_def)
    self.assertNotIn("T", node_def.attr)
    self.assertNotIn("Tout", node_def.attr)
    self.assertTrue(meta_graph_def.meta_info_def.stripped_default_attrs)

    # strip_default_attrs is disabled.
    meta_graph_def, _ = meta_graph.export_scoped_meta_graph(
        graph_def=ops.get_default_graph().as_graph_def(),
        strip_default_attrs=False)
    node_def = test_util.get_node_def_from_graph("complex",
                                                 meta_graph_def.graph_def)
    self.assertIn("T", node_def.attr)
    self.assertIn("Tout", node_def.attr)
    self.assertFalse(meta_graph_def.meta_info_def.stripped_default_attrs)

# When inputs to the Complex Op are float64 instances, "T" maps to float64
# and "Tout" maps to complex128. Since these attr values don't map to their
# defaults, they must not be stripped.
with self.session(graph=ops.Graph()):
    real_num = constant_op.constant(1.0, dtype=dtypes.float64, name="real")
    imag_num = constant_op.constant(2.0, dtype=dtypes.float64, name="imag")
    math_ops.complex(real_num, imag_num, name="complex")
    meta_graph_def, _ = meta_graph.export_scoped_meta_graph(
        graph_def=ops.get_default_graph().as_graph_def(),
        strip_default_attrs=True)
    node_def = test_util.get_node_def_from_graph("complex",
                                                 meta_graph_def.graph_def)
    self.assertEqual(node_def.attr["T"].type, dtypes.float64)
    self.assertEqual(node_def.attr["Tout"].type, dtypes.complex128)
    self.assertTrue(meta_graph_def.meta_info_def.stripped_default_attrs)
