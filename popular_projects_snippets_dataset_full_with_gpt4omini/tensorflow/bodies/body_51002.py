# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_clear_devices")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    # Specify a device and save a variable.
    with session.Session(
        target="",
        config=config_pb2.ConfigProto(device_count={"CPU": 2})) as sess:
        with sess.graph.device("/cpu:0"):
            self._init_and_validate_variable(sess, "v", 42)
            builder.add_meta_graph_and_variables(
                sess, [tag_constants.TRAINING], clear_devices=True)

      # Save the SavedModel to disk.
    builder.save()

    # Restore the graph with a single predefined tag whose variables were
    # saved without any device information.
    with self.session(graph=ops.Graph()) as sess:
        loader.load(sess, [tag_constants.TRAINING], export_dir)
        self.assertEqual(42, self._eval("v"))
