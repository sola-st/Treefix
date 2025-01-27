# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_duplicate_assets")
builder = saved_model_builder._SavedModelBuilder(export_dir)

with ops.Graph().as_default():
    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)

        # Build an asset collection with `foo.txt` that has `foo` specific
        # content.
        asset_list = self._build_asset_collection("foo.txt", "content_foo",
                                                  "asset_file_tensor")

        # Add the asset collection as part of the graph with tag "foo".
        builder.add_meta_graph_and_variables(
            sess, ["foo"], assets_list=asset_list)

    with self.session(graph=ops.Graph()) as sess:
        self._init_and_validate_variable(sess, "v", 42)

        # Build an asset collection with `foo.txt` that has `bar` specific
        # content.
        asset_list = self._build_asset_collection("foo.txt", "content_bar",
                                                  "asset_file_tensor")

        # Add the asset collection as part of the graph with tag "bar".
        builder.add_meta_graph(["bar"], assets_list=asset_list)

    # Save the SavedModel to disk.
    builder.save()

    # Check assets restored for graph with tag "foo".
    with self.session(graph=ops.Graph()) as sess:
        foo_graph = loader.load(sess, ["foo"], export_dir)
        self._validate_assets(export_dir, foo_graph.asset_file_def, "foo.txt",
                              "content_foo", "asset_file_tensor:0")

    # Check assets restored for graph with tag "bar".
    with self.session(graph=ops.Graph()) as sess:
        bar_graph = loader.load(sess, ["bar"], export_dir)

        # Validate the assets for `bar` graph. `foo.txt` should contain the
        # original contents corresponding to `foo` graph since an asset with the
        # same name across multiple graphs is only stored the first time
        self._validate_assets(export_dir, bar_graph.asset_file_def, "foo.txt",
                              "content_foo", "asset_file_tensor:0")
