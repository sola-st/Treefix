# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_def_utils_impl.py
"""Creates a signature for training and eval data.

  This function produces signatures that describe the inputs and outputs
  of a supervised process, such as training or evaluation, that
  results in loss, metrics, and the like. Note that this function only requires
  inputs to be not None.

  Args:
    method_name: Method name of the SignatureDef as a string.
    inputs: dict of string to `Tensor`.
    loss: dict of string to `Tensor` representing computed loss.
    predictions: dict of string to `Tensor` representing the output predictions.
    metrics: dict of string to `Tensor` representing metric ops.

  Returns:
    A train- or eval-flavored signature_def.

  Raises:
    ValueError: If inputs or outputs is `None`.
  """
if inputs is None or not inputs:
    raise ValueError(f'{method_name} `inputs` cannot be None or empty.')

signature_inputs = {key: utils.build_tensor_info(tensor)
                    for key, tensor in inputs.items()}

signature_outputs = {}
for output_set in (loss, predictions, metrics):
    if output_set is not None:
        sig_out = {key: utils.build_tensor_info(tensor)
                   for key, tensor in output_set.items()}
        signature_outputs.update(sig_out)

signature_def = build_signature_def(
    signature_inputs, signature_outputs, method_name)

exit(signature_def)
