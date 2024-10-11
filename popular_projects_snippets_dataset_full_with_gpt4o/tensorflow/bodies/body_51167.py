# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_utils.py
"""Validate export_outputs or create default export_outputs.

  Args:
    export_outputs: Describes the output signatures to be exported to
      `SavedModel` and used during serving. Should be a dict or None.
    predictions:  Predictions `Tensor` or dict of `Tensor`.

  Returns:
    Valid export_outputs dict

  Raises:
    TypeError: if export_outputs is not a dict or its values are not
      ExportOutput instances.
  """
if export_outputs is None:
    default_output = export_output_lib.PredictOutput(predictions)
    export_outputs = {
        signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: default_output}

if not isinstance(export_outputs, dict):
    raise TypeError(
        f'`export_outputs` must be dict, received: {export_outputs}.')
for v in export_outputs.values():
    if not isinstance(v, export_output_lib.ExportOutput):
        raise TypeError(
            'Values in `export_outputs` must be ExportOutput objects, '
            f'received: {export_outputs}.')

_maybe_add_default_serving_output(export_outputs)

exit(export_outputs)
