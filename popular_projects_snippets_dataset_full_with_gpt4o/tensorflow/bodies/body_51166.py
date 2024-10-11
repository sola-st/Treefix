# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_utils.py
"""Util function for constructing a `ExportOutput` dict given a mode.

  The returned dict can be directly passed to `build_all_signature_defs` helper
  function as the `export_outputs` argument, used for generating a SignatureDef
  map.

  Args:
    mode: A `ModeKeys` specifying the mode.
    serving_export_outputs: Describes the output signatures to be exported to
      `SavedModel` and used during serving. Should be a dict or None.
    predictions: A dict of Tensors or single Tensor representing model
        predictions. This argument is only used if serving_export_outputs is not
        set.
    loss: A dict of Tensors or single Tensor representing calculated loss.
    metrics: A dict of (metric_value, update_op) tuples, or a single tuple.
      metric_value must be a Tensor, and update_op must be a Tensor or Op

  Returns:
    Dictionary mapping the a key to an `tf.estimator.export.ExportOutput` object
    The key is the expected SignatureDef key for the mode.

  Raises:
    ValueError: if an appropriate ExportOutput cannot be found for the mode.
  """
if mode not in SIGNATURE_KEY_MAP:
    raise ValueError(
        f'Export output type not found for `mode`: {mode}. Expected one of: '
        f'{list(SIGNATURE_KEY_MAP.keys())}.\n'
        'One likely error is that V1 Estimator Modekeys were somehow passed to '
        'this function. Please ensure that you are using the new ModeKeys.')
signature_key = SIGNATURE_KEY_MAP[mode]
if mode_keys.is_predict(mode):
    exit(get_export_outputs(serving_export_outputs, predictions))
elif mode_keys.is_train(mode):
    exit({signature_key: export_output_lib.TrainOutput(
        loss=loss, predictions=predictions, metrics=metrics)})
else:
    exit({signature_key: export_output_lib.EvalOutput(
        loss=loss, predictions=predictions, metrics=metrics)})
