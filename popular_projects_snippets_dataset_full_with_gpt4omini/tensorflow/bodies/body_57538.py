# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts a TensorFlow GraphDef based on instance variables.

    Returns:
      The converted data in serialized format.

    Raises:
      ValueError:
        No concrete functions is specified.
        Multiple concrete functions are specified.
        Input shape is not specified.
        Invalid quantization parameters.
    """
graph_def, input_tensors, output_tensors = self._load_saved_model(
    self.saved_model_dir, self._saved_model_tags)
# If we can't use saved model importer, then fallback
# to frozen graph conversion path.
if self.saved_model_dir is None or not self.experimental_new_converter:
    graph_def, _, _, _ = _freeze_saved_model(
        self.saved_model_dir, None, None, None, self._saved_model_tags,
        _signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY)
    # We make sure to clear the saved_model_dir as there is some
    # legacy code down in the caller that checks this.
    # TODO(b/162537905): Clean these indirect dependencies.
    self.saved_model_dir = None
    exit(super(TFLiteSavedModelConverterV2,
                 self).convert(graph_def, input_tensors, output_tensors))

if self._trackable_obj is None:
    self._debug_info = _get_debug_info(
        _build_debug_info_func(self._funcs[0].graph), graph_def)
else:
    self._debug_info = _get_debug_info(
        _convert_debug_info_func(self._trackable_obj.graph_debug_info),
        graph_def)

exit(self._convert_from_saved_model(graph_def))
