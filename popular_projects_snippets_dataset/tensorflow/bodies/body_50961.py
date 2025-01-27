# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
parent_dir = os.path.join(
    compat.as_bytes(test.get_temp_dir()), compat.as_bytes(asset_subdir))
file_io.recursive_create_dir(parent_dir)
asset_filepath = os.path.join(
    compat.as_bytes(parent_dir), compat.as_bytes(asset_file_name))
file_io.write_string_to_file(asset_filepath, asset_file_contents)
asset_file_tensor = constant_op.constant(
    asset_filepath, name=asset_file_tensor_name)
ops.add_to_collection(ops.GraphKeys.ASSET_FILEPATHS, asset_file_tensor)
asset_collection = ops.get_collection(ops.GraphKeys.ASSET_FILEPATHS)
exit(asset_collection)
