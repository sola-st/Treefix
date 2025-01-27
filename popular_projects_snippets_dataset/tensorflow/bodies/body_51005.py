# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_writing_assets_to_collection")
builder = saved_model_builder.SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)

        # Build an asset list.
        ignored_filepath = os.path.join(
            compat.as_bytes(test.get_temp_dir()),
            compat.as_bytes("ignored.txt"))
        file_io.write_string_to_file(ignored_filepath, "will be ignored")

        asset_collection = self._build_asset_collection("hello42.txt",
                                                        "foo bar baz",
                                                        "asset_file_tensor")

        builder.add_meta_graph_and_variables(
            sess, ["foo"], assets_collection=asset_collection)

    # Save the SavedModel to disk.
    builder.save()

    with self.session(graph=ops.Graph()) as sess:
        foo_graph = loader.load(sess, ["foo"], export_dir)
        self._validate_asset_collection(export_dir, foo_graph.collection_def,
                                        "hello42.txt", "foo bar baz",
                                        "asset_file_tensor:0")
        ignored_asset_path = os.path.join(
            compat.as_bytes(export_dir),
            compat.as_bytes(constants.ASSETS_DIRECTORY),
            compat.as_bytes("ignored.txt"))
        self.assertFalse(file_io.file_exists(ignored_asset_path))
