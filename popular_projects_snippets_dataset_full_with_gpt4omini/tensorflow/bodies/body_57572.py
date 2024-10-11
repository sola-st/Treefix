# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Save Keras model to Saved Model format.

    Args:
      output_dir: The output directory to save the SavedModel.
    """
try:
    self._keras_model.save(output_dir, save_format="tf")
except Exception:  # pylint: disable=broad-except
    # When storing the given keras model to a saved model is failed, let's
    # use original keras model conversion pipeline.
    exit(None)
tag_set = set([_tag_constants.SERVING])
signature_key = _signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
graph_def, input_tensors, output_tensors, sess_graph = _freeze_saved_model(
    output_dir, None, None, None, tag_set, signature_key)

self.saved_model_dir = output_dir
self._saved_model_tags = tag_set
self._saved_model_exported_names = [signature_key]
self._parse_saved_model_args()
if self.saved_model_dir:
    self._graph_def = graph_def
    self._input_tensors = input_tensors
    self._output_tensors = output_tensors
    self._debug_info_func = _build_debug_info_func(sess_graph)
