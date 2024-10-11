# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
# Test that we are able to save a model that contains a custom op with a
# custom namespace when the user has not explicitly specified a namespace
# whitelist (i.e. that we default to allowing all custom ops when saving
# and no whitelist is specified, rather than throwing an exception).
graph_def = graph_pb2.GraphDef()
text_format.Parse("node { name: 'A' op: 'Test>CustomOp' }", graph_def)
save._verify_ops(graph_def, namespace_whitelist=None)

# If the user passes an empty list for the namespace whitelist rather than
# nothing, we should then throw an exception if a custom op is used.
with self.assertRaisesRegex(
    ValueError, "Attempted to save ops from non-whitelisted namespaces"):
    save._verify_ops(graph_def, [])
