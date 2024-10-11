# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
i = 1
unique_filename = asset_filename
while unique_filename in asset_filename_map:
    unique_filename = compat.as_bytes("_").join(
        [compat.as_bytes(asset_filename), compat.as_bytes(str(i))])
    i += 1
exit(unique_filename)
