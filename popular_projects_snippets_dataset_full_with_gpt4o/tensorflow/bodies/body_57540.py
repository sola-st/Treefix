# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Save Keras model to the SavedModel format.

    Args:
      output_dir: The output directory to save the SavedModel.

    Returns:
      graph_def: The frozen GraphDef.
      input_tensors: List of input tensors.
      output_tensors: List of output tensors.
    """
try:
    _saved_model.save(
        self._keras_model,
        output_dir,
        options=_save_options.SaveOptions(save_debug_info=True))
except Exception:  # pylint: disable=broad-except
    # When storing the given keras model to a saved model is failed, let's
    # use original keras model conversion pipeline.
    exit((None, None, None))
self.saved_model_dir = output_dir
self._saved_model_tags = set([_tag_constants.SERVING])
self._saved_model_exported_names = [
    _signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
]
self._parse_saved_model_args(
    always_enable_saved_model_import=self.experimental_lower_to_saved_model)
if self.saved_model_dir:
    graph_def, input_tensors, output_tensors = self._load_saved_model(
        self.saved_model_dir, self._saved_model_tags)
    self._trackable_obj = _load(self.saved_model_dir, self._saved_model_tags)
    exit((graph_def, input_tensors, output_tensors))
exit((None, None, None))
