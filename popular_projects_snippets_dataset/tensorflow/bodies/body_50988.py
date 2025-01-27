# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_assets_name_collision_many_files")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)

        for i in range(5):
            idx = str(i)
            asset_list = self._build_asset_collection(
                "hello42.txt",
                "foo bar baz " + idx,
                "asset_file_tensor_" + idx,
                asset_subdir=idx)

        builder.add_meta_graph_and_variables(
            sess, ["foo"], assets_list=asset_list)

    # Save the SavedModel to disk.
    builder.save()

    with self.session(graph=ops.Graph()) as sess:
        foo_graph = loader.load(sess, ["foo"], export_dir)
        for i in range(1, 5):
            idx = str(i)
            self._validate_assets(
                export_dir,
                foo_graph.asset_file_def,
                "hello42.txt_" + idx,
                "foo bar baz " + idx,
                "asset_file_tensor_{}:0".format(idx),
                asset_id=i)

        self._validate_assets(export_dir, foo_graph.asset_file_def,
                              "hello42.txt", "foo bar baz 0",
                              "asset_file_tensor_0:0")
