# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_strip_default_attrs")
builder = saved_model_builder.SavedModelBuilder(export_dir)

# Add a graph with two float32 variables and a Complex Op composing them
# with strip_default_attrs enabled.
with session.Session(graph=ops.Graph()) as sess:
    real_num = variables.VariableV1(1.0, dtype=dtypes.float32, name="real")
    imag_num = variables.VariableV1(2.0, dtype=dtypes.float32, name="imag")
    math_ops.complex(real_num, imag_num, name="complex")
    self.evaluate(variables.global_variables_initializer())
    builder.add_meta_graph_and_variables(
        sess, ["foo"], strip_default_attrs=True)

# Add a graph with the same float32 variables and a Complex Op composing
# them with strip_default_attrs disabled.
with session.Session(graph=ops.Graph()) as sess:
    real_num = variables.VariableV1(1.0, dtype=dtypes.float32, name="real")
    imag_num = variables.VariableV1(2.0, dtype=dtypes.float32, name="imag")
    math_ops.complex(real_num, imag_num, name="complex")
    self.evaluate(variables.global_variables_initializer())
    builder.add_meta_graph(["bar"], strip_default_attrs=False)

# Save the SavedModel to disk in text format.
builder.save(as_text=True)

# Loading graph "foo" via the loader must restore the defaults for the
# "Complex" node based on the "Complex" OpDef in the Op registry.
sess = session.Session(graph=ops.Graph())
meta_graph_def = loader.load(sess, ["foo"], export_dir)
complex_node = test_util.get_node_def_from_graph("complex",
                                                 meta_graph_def.graph_def)
self.assertIn("T", complex_node.attr)
self.assertIn("Tout", complex_node.attr)

# Load graph "foo" from disk as-is to verify default attrs are stripped.
saved_model_pb = loader_impl.parse_saved_model(export_dir)
self.assertIsNotNone(saved_model_pb)

meta_graph_foo_def = None
meta_graph_bar_def = None
for meta_graph_def in saved_model_pb.meta_graphs:
    if set(meta_graph_def.meta_info_def.tags) == set(["foo"]):
        meta_graph_foo_def = meta_graph_def
    elif set(meta_graph_def.meta_info_def.tags) == set(["bar"]):
        meta_graph_bar_def = meta_graph_def

self.assertIsNotNone(meta_graph_foo_def)
self.assertIsNotNone(meta_graph_bar_def)

# "Complex" Op has 2 attributes with defaults:
#   o "T"    : float32.   (input type)
#   o "Tout" : complex64. (output type)

# "Complex" Op in graph "foo" shouldn't have attributes "T" and "Tout".
# Graph "foo" was saved with strip_default_attrs set to True.
node_def = test_util.get_node_def_from_graph("complex",
                                             meta_graph_foo_def.graph_def)
self.assertNotIn("T", node_def.attr)
self.assertNotIn("Tout", node_def.attr)

# "Complex" Op in graph "bar" must have attributes "T" and "Tout".
# Graph "bar" was saved with strip_default_attrs set to False.
node_def = test_util.get_node_def_from_graph("complex",
                                             meta_graph_bar_def.graph_def)
self.assertIn("T", node_def.attr)
self.assertIn("Tout", node_def.attr)
