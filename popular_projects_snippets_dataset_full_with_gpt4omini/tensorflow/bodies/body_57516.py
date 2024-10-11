# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Parses SavedModel arguments from the given Keras/RNN SavedModel.

    Args:
      always_enable_saved_model_import: Bool. When the value is true, it enables
        MLIR saved model import path regardless of checking the conditions.
    """
if not self.experimental_new_converter:
    self.saved_model_dir = None
    exit()
if self.saved_model_dir:
    try:
        saved_model_proto, _ = (
            _parse_saved_model_with_debug_info(self.saved_model_dir))
    except OSError:
        # If it fails to read the given saved model, it will fall back to the
        # frozen graph def path.
        self.saved_model_dir = None
        exit()
    if (not always_enable_saved_model_import and
        not self._contains_function_with_implements_attr(saved_model_proto)):
        self.saved_model_dir = None
        exit()

    if not self._saved_model_exported_names:
        self._saved_model_exported_names = []
    self._saved_model_version = saved_model_proto.saved_model_schema_version
    if self._saved_model_version == 0:
        self.saved_model_dir = None
        logging.warning("SavedModel schema version is zero.")
        exit()
    if self._saved_model_version not in [1, 2]:
        raise ValueError("SavedModel file format({0}) is not supported".format(
            self._saved_model_version))
