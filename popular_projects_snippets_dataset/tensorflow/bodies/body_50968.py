# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
with self.session(graph=ops.Graph()) as sess:
    self._init_and_validate_variable(sess, "v", 42)

    foo_signature = signature_def_utils.build_signature_def(
        dict(), {"foo_key": valid_tensor_info}, "foo")
    self.assertRaises(
        KeyError,
        builder.add_meta_graph_and_variables,
        sess, ["foo"],
        signature_def_map={invalid_key: foo_signature})
