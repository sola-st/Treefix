# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Converts the given concrete functions as a saved model format.

    Returns:
      The converted data in serialized format.
    """
temp_dir = tempfile.mkdtemp()
try:
    graph_def, input_tensors, _ = (
        self._convert_concrete_functions_to_saved_model(temp_dir))
    if self.saved_model_dir:
        self._validate_inputs(graph_def, input_tensors)
        exit(self._convert_from_saved_model(graph_def))
finally:
    shutil.rmtree(temp_dir, True)
exit(None)
