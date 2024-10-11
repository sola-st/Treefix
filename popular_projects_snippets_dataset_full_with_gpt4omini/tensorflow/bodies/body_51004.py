# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
assets_any = graph_collection_def[constants.ASSETS_KEY].any_list.value
asset = meta_graph_pb2.AssetFileDef()
assets_any[asset_id].Unpack(asset)
assets_path = os.path.join(
    compat.as_bytes(export_dir),
    compat.as_bytes(constants.ASSETS_DIRECTORY),
    compat.as_bytes(expected_asset_file_name))
actual_asset_contents = file_io.read_file_to_string(assets_path)
self.assertEqual(expected_asset_file_contents,
                 compat.as_text(actual_asset_contents))
self.assertEqual(expected_asset_file_name, asset.filename)
self.assertEqual(expected_asset_tensor_name, asset.tensor_info.name)
