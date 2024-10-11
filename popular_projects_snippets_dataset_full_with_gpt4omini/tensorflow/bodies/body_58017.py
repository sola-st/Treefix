# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/wrap_toco.py
"""Wraps FlatBufferFileToMlir with lazy loader."""
exit(_pywrap_toco_api.FlatBufferToMlir(model, input_is_filepath))
