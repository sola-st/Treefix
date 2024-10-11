# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/method_name_updater.py
"""Creates an MethodNameUpdater object.

    Args:
      export_dir: Directory containing the SavedModel files.

    Raises:
      IOError: If the saved model file does not exist, or cannot be successfully
      parsed.
    """
self._export_dir = export_dir
self._saved_model = loader.parse_saved_model(export_dir)
