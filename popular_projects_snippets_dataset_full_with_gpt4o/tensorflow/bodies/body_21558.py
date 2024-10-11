# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
"""Verifies that default valued attrs are stripped, unless disabled."""

# With strip_default_attrs enabled, attributes "T" (float32) and "Tout"
# (complex64) in the "Complex" op must be removed.
# train.Saver and train.export_meta_graph are V1 only APIs.
with ops_lib.Graph().as_default(), self.cached_session():
    real_num = variables.VariableV1(1.0, dtype=dtypes.float32, name="real")
    imag_num = variables.VariableV1(2.0, dtype=dtypes.float32, name="imag")
    math_ops.complex(real_num, imag_num, name="complex")

    save = saver_module.Saver({"real_num": real_num, "imag_num": imag_num})
    variables.global_variables_initializer()

    meta_graph_def = save.export_meta_graph(strip_default_attrs=True)
    node_def = test_util.get_node_def_from_graph("complex",
                                                 meta_graph_def.graph_def)
    self.assertNotIn("T", node_def.attr)
    self.assertNotIn("Tout", node_def.attr)

# With strip_default_attrs disabled, attributes "T" (float32) and "Tout"
# (complex64) in the "Complex" op must *not* be removed, even if they map
# to their defaults.
with ops_lib.Graph().as_default(), self.session():
    real_num = variables.VariableV1(1.0, dtype=dtypes.float32, name="real")
    imag_num = variables.VariableV1(2.0, dtype=dtypes.float32, name="imag")
    math_ops.complex(real_num, imag_num, name="complex")

    save = saver_module.Saver({"real_num": real_num, "imag_num": imag_num})
    variables.global_variables_initializer()

    meta_graph_def = save.export_meta_graph(strip_default_attrs=False)
    node_def = test_util.get_node_def_from_graph("complex",
                                                 meta_graph_def.graph_def)
    self.assertIn("T", node_def.attr)
    self.assertIn("Tout", node_def.attr)
