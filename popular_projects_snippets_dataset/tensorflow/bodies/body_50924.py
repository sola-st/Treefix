# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
"""Creates prediction signature from given inputs and outputs.

  This function produces signatures intended for use with the TensorFlow Serving
  Predict API (tensorflow_serving/apis/prediction_service.proto). This API
  imposes no constraints on the input and output types.

  Args:
    inputs: dict of string to `Tensor`.
    outputs: dict of string to `Tensor`.

  Returns:
    A prediction-flavored signature_def.

  Raises:
    ValueError: If inputs or outputs is `None`.
  """
if inputs is None or not inputs:
    raise ValueError('Prediction `inputs` cannot be None or empty.')
if outputs is None or not outputs:
    raise ValueError('Prediction `outputs` cannot be None or empty.')

signature_inputs = {key: utils.build_tensor_info(tensor)
                    for key, tensor in inputs.items()}
signature_outputs = {key: utils.build_tensor_info(tensor)
                     for key, tensor in outputs.items()}

signature_def = build_signature_def(
    signature_inputs, signature_outputs,
    signature_constants.PREDICT_METHOD_NAME)

exit(signature_def)
