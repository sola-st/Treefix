# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
test_dir = _TestDir("no_variables")
filename = os.path.join(test_dir, "metafile")

input_feed_value = -10  # Arbitrary input value for feed_dict.

orig_graph = ops.Graph()
with self.session(graph=orig_graph) as sess:
    # Create a minimal graph with zero variables.
    input_tensor = array_ops.placeholder(
        dtypes.float32, shape=[], name="input")
    offset = constant_op.constant(42, dtype=dtypes.float32, name="offset")
    output_tensor = math_ops.add(input_tensor, offset, name="add_offset")

    # Add input and output tensors to graph collections.
    ops.add_to_collection("input_tensor", input_tensor)
    ops.add_to_collection("output_tensor", output_tensor)

    output_value = sess.run(output_tensor, {input_tensor: input_feed_value})
    self.assertEqual(output_value, 32)

    # Generates MetaGraphDef.
    meta_graph_def, var_list = meta_graph.export_scoped_meta_graph(
        filename=filename,
        graph_def=ops.get_default_graph().as_graph_def(add_shapes=True),
        collection_list=["input_tensor", "output_tensor"],
        saver_def=None)
    self.assertTrue(meta_graph_def.HasField("meta_info_def"))
    self.assertNotEqual(meta_graph_def.meta_info_def.tensorflow_version, "")
    self.assertNotEqual(meta_graph_def.meta_info_def.tensorflow_git_version,
                        "")
    self.assertEqual({}, var_list)

# Create a clean graph and import the MetaGraphDef nodes.
new_graph = ops.Graph()
with self.session(graph=new_graph) as sess:
    # Import the previously export meta graph.
    meta_graph.import_scoped_meta_graph(filename)

    # Re-exports the current graph state for comparison to the original.
    new_meta_graph_def, _ = meta_graph.export_scoped_meta_graph(filename +
                                                                "_new")
    test_util.assert_meta_graph_protos_equal(self, meta_graph_def,
                                             new_meta_graph_def)

    # Ensures that we can still get a reference to our graph collections.
    new_input_tensor = ops.get_collection("input_tensor")[0]
    new_output_tensor = ops.get_collection("output_tensor")[0]
    # Verifies that the new graph computes the same result as the original.
    new_output_value = sess.run(new_output_tensor,
                                {new_input_tensor: input_feed_value})
    self.assertEqual(new_output_value, output_value)
