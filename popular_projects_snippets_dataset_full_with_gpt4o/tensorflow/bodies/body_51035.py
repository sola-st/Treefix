# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_impl.py
"""Creates a `SavedModelLoader`.

    Args:
      export_dir: Directory in which the SavedModel protocol buffer and
        variables to be loaded are located.
    """
self._export_dir = export_dir
self._variables_path = path_helpers.get_variables_path(export_dir)
self._saved_model = parse_saved_model(export_dir)
