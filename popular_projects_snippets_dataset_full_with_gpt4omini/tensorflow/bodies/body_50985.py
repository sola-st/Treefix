# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_assets_name_collision_diff_file")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)

        asset_list = self._build_asset_collection(
            "hello42.txt", "foo bar bak", "asset_file_tensor", asset_subdir="1")

        asset_list = self._build_asset_collection(
            "hello42.txt",
            "foo bar baz",
            "asset_file_tensor_1",
            asset_subdir="2")

        builder.add_meta_graph_and_variables(
            sess, ["foo"], assets_list=asset_list)

    # Save the SavedModel to disk.
    builder.save()

    with self.session(graph=ops.Graph()) as sess:
        foo_graph = loader.load(sess, ["foo"], export_dir)
        self._validate_assets(export_dir, foo_graph.asset_file_def,
                              "hello42.txt", "foo bar bak",
                              "asset_file_tensor:0")
        self._validate_assets(
            export_dir,
            foo_graph.asset_file_def,
            "hello42.txt_1",
            "foo bar baz",
            "asset_file_tensor_1:0",
            asset_id=1)
