# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/path_helpers.py
exit(file_io.join(
    compat.as_bytes(compat.path_to_str(export_dir)),
    compat.as_bytes(constants.SAVED_MODEL_FILENAME_PBTXT)))
