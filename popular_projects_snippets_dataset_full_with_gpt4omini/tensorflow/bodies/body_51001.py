# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_scoped_assets")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    # Build a SavedModel with a variable, an asset, and a constant tensor.
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)
        asset_list = self._build_asset_collection("foo.txt", "content_foo",
                                                  "asset_file_tensor")
        constant_op.constant("constant value", name="constant_tensor_name")
        builder.add_meta_graph_and_variables(
            sess, ["tag_name"], assets_list=asset_list)

        # Save the asset file path for later comparison.
        asset_file_path = asset_list[0].eval()

    # Save the SavedModel to disk.
    builder.save()

    with self.session(graph=ops.Graph()) as sess:
        # Restore the SavedModel under an import_scope in a new graph/session.
        graph_proto = loader.load(
            sess, ["tag_name"], export_dir, import_scope="scope_name")

        # The loaded variable tensor should be scoped, but its contents should
        # be unchanged.
        self.assertEqual(
            "scope_name/v:0",
            ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)[0].name)
        self.assertEqual(42, self._eval("scope_name/v"))

        # The loaded asset tensor should be scoped, but the asset file path and
        # contents should be unchanged.
        asset_list = ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS)
        self.assertEqual(1, len(asset_list))
        self.assertEqual(asset_file_path, asset_list[0].eval())
        self.assertEqual("scope_name/asset_file_tensor:0", asset_list[0].name)
        # The static asset data inside graph_proto.collection_def should not be
        # scoped.
        self._validate_assets(export_dir, graph_proto.asset_file_def, "foo.txt",
                              "content_foo", "asset_file_tensor:0")

        # The constant tensor should be scoped, but its contents should be
        # unchanged.
        self.assertEqual(
            compat.as_bytes("constant value"),
            ops.get_default_graph().get_tensor_by_name(
                "scope_name/constant_tensor_name:0").eval())
