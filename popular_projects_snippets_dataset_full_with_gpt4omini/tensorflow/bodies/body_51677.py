# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/simple_save_test.py
"""Test simple_save that uses the default parameters."""
export_dir = os.path.join(test.get_temp_dir(),
                          "test_simple_save")

# Force the test to run in graph mode.
# This tests a deprecated v1 API that both requires a session and uses
# functionality that does not work with eager tensors (such as
# build_tensor_info as called by predict_signature_def).
with ops.Graph().as_default():
    # Initialize input and output variables and save a prediction graph using
    # the default parameters.
    with self.session(graph=ops.Graph()) as sess:
        var_x = self._init_and_validate_variable("var_x", 1)
        var_y = self._init_and_validate_variable("var_y", 2)
        inputs = {"x": var_x}
        outputs = {"y": var_y}
        simple_save.simple_save(sess, export_dir, inputs, outputs)

    # Restore the graph with a valid tag and check the global variables and
    # signature def map.
    with self.session(graph=ops.Graph()) as sess:
        graph = loader.load(sess, [tag_constants.SERVING], export_dir)
        collection_vars = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)

        # Check value and metadata of the saved variables.
        self.assertEqual(len(collection_vars), 2)
        self.assertEqual(1, collection_vars[0].eval())
        self.assertEqual(2, collection_vars[1].eval())
        self._check_variable_info(collection_vars[0], var_x)
        self._check_variable_info(collection_vars[1], var_y)

        # Check that the appropriate signature_def_map is created with the
        # default key and method name, and the specified inputs and outputs.
        signature_def_map = graph.signature_def
        self.assertEqual(1, len(signature_def_map))
        self.assertEqual(signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY,
                         list(signature_def_map.keys())[0])

        signature_def = signature_def_map[
            signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
        self.assertEqual(signature_constants.PREDICT_METHOD_NAME,
                         signature_def.method_name)

        self.assertEqual(1, len(signature_def.inputs))
        self._check_tensor_info(signature_def.inputs["x"], var_x)
        self.assertEqual(1, len(signature_def.outputs))
        self._check_tensor_info(signature_def.outputs["y"], var_y)
