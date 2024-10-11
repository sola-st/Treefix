# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
# TODO(kathywu): Add test that saves out SavedModel with a custom op when
# the ">" character is allowed in op names.
graph_def = graph_pb2.GraphDef()
text_format.Parse("node { name: 'A' op: 'Test>CustomOp' }", graph_def)
with self.assertRaisesRegex(
    ValueError, "Attempted to save ops from non-whitelisted namespaces"):
    save._verify_ops(graph_def, [])
save._verify_ops(graph_def, ["Test"])

# Test with multiple carrots in op name.
text_format.Parse("node { name: 'A' op: 'Test>>A>CustomOp' }", graph_def)
with self.assertRaisesRegex(
    ValueError, "Attempted to save ops from non-whitelisted namespaces"):
    save._verify_ops(graph_def, [])
save._verify_ops(graph_def, ["Test"])
