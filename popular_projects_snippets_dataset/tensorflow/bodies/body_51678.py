# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/builder_impl.py
self._saved_model = saved_model_pb2.SavedModel()
self._saved_model.saved_model_schema_version = (
    constants.SAVED_MODEL_SCHEMA_VERSION)

self._export_dir = export_dir
if file_io.file_exists(export_dir):
    if file_io.list_directory(export_dir):
        raise AssertionError(
            f"Export directory {export_dir} already exists, and isn't empty. "
            "Please choose a different export directory, or delete all the "
            "contents of the specified directory.")
else:
    file_io.recursive_create_dir(self._export_dir)

# Boolean to track whether variables and assets corresponding to the
# SavedModel have been saved. Specifically, the first meta graph to be added
# MUST use the add_meta_graph_and_variables() API. Subsequent add operations
# on the SavedModel MUST use the add_meta_graph() API which does not save
# weights.
self._has_saved_variables = False
self._saved_asset_files = set()
