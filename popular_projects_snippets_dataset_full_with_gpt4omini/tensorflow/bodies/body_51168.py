# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_utils.py
"""Add a default serving output to the export_outputs if not present.

  Args:
    export_outputs: Describes the output signatures to be exported to
      `SavedModel` and used during serving. Should be a dict.

  Returns:
    export_outputs dict with default serving signature added if necessary

  Raises:
    ValueError: if multiple export_outputs were provided without a default
      serving key.
  """
if len(export_outputs) == 1:
    (key, value), = export_outputs.items()
    if key != signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
        export_outputs[
            signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY] = value
if len(export_outputs) > 1:
    if (signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
        not in export_outputs):
        raise ValueError(
            'Multiple `export_outputs` were provided, but none of them are '
            'specified as the default. Use'
            '`tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY` to '
            'specify a default.')

exit(export_outputs)
