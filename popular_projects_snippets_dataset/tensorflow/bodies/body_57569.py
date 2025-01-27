# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Constructor for TFLiteConverter.

    Args:
      saved_model_dir: Directory of the SavedModel.
      saved_model_tags: Set of tags identifying the MetaGraphDef within the
        SavedModel to analyze. All tags in the tag set must be present. (default
        {tf.saved_model.SERVING}).
      saved_model_exported_names: Names to be exported when the saved model
        import path is on.
      experimental_debug_info_func: An experimental function to retrieve the
        graph debug info for a set of nodes from the `graph_def`.

    Raises:
      ValueError: Invalid arguments.
    """
super(TFLiteSavedModelConverter,
      self).__init__(experimental_debug_info_func)
self.saved_model_dir = saved_model_dir
self._saved_model_tags = saved_model_tags
self._saved_model_exported_names = saved_model_exported_names

signature_key = _signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY

if len(self._saved_model_exported_names) != 1:
    raise ValueError("Only support a single signature key.")

signature_key = self._saved_model_exported_names[0]

result = _freeze_saved_model(self.saved_model_dir, None, None, None,
                             self._saved_model_tags, signature_key)
self._graph_def = result[0]
self._input_tensors = result[1]
self._output_tensors = result[2]
self._parse_saved_model_args()
