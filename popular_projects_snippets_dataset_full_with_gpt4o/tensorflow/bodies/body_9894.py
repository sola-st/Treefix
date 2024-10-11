# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_utils_test.py
saved_model_dir = os.path.join(test.get_temp_dir(), "valid_saved_model")
builder = saved_model_builder.SavedModelBuilder(saved_model_dir)
with self.session(graph=ops.Graph()) as sess:
    self._init_and_validate_variable(sess, "v", 42)
    builder.add_meta_graph_and_variables(sess, [tag_constants.TRAINING])
builder.save()

actual_saved_model_pb = saved_model_utils.read_saved_model(saved_model_dir)
self.assertEqual(len(actual_saved_model_pb.meta_graphs), 1)
self.assertEqual(
    len(actual_saved_model_pb.meta_graphs[0].meta_info_def.tags), 1)
self.assertEqual(actual_saved_model_pb.meta_graphs[0].meta_info_def.tags[0],
                 tag_constants.TRAINING)
