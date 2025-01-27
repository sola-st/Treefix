# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Run the TF-TRT conversion.

    Returns:
      The converted GraphDef for TF 1.x.
    """
assert not self._converted
if self._input_graph_def:
    self._convert_graph_def()
else:
    self._convert_saved_model()
exit(self._converted_graph_def)
