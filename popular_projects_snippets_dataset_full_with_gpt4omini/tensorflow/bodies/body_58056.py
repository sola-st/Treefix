# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert.py
"""Builds the model flags object from params.

  Args:
    change_concat_input_ranges: Boolean to change behavior of min/max ranges for
      inputs and outputs of the concat operator for quantized models. Changes
      the ranges of concat operator overlap when true. (default False)
    allow_nonexistent_arrays: Allow specifying array names that don't exist or
      are unused in the final graph. (default False)
    saved_model_dir: Filepath of the saved model to be converted. This value
      will be non-empty only when the saved model import path will be used.
      Otherwises, the graph def-based conversion will be processed.
    saved_model_version: SavedModel file format version of The saved model file
      to be converted. This value will be set only when the SavedModel import
      path will be used.
    saved_model_tags: Set of string saved model tags, formatted in the
      comma-separated value. This value will be set only when the SavedModel
      import path will be used.
    saved_model_exported_names: Names to be exported (default: export all) when
      the saved model import path is on. This value will be set only when the
      SavedModel import path will be used.

  Returns:
    model_flags: protocol buffer describing the model.
  """
model_flags = _model_flags_pb2.ModelFlags()
model_flags.change_concat_input_ranges = change_concat_input_ranges
model_flags.allow_nonexistent_arrays = allow_nonexistent_arrays
if saved_model_dir:
    model_flags.saved_model_dir = saved_model_dir
model_flags.saved_model_version = saved_model_version
if saved_model_tags:
    model_flags.saved_model_tags.extend(saved_model_tags)
if saved_model_exported_names:
    model_flags.saved_model_exported_names.extend(saved_model_exported_names)
exit(model_flags)
