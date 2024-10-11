# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Runs the representative dataset through a function for calibration.

  NOTE: This is intended to be run in graph mode (TF1).

  The function is identified by the SignatureDef.

  Args:
    sess: The Session object to run the function in.
    signature_def: A SignatureDef that identifies a function by specifying the
      inputs and outputs.
    representative_dataset: The representative dataset to run through the
      function.
  """
output_tensor_names = [
    output_tensor_info.name
    for output_tensor_info in signature_def.outputs.values()
]

sample_validator = _create_sample_validator(
    expected_input_keys=signature_def.inputs.keys()
)

for sample in map(
    sample_validator, _log_sample_num_for_calibration(representative_dataset)
):
    # Create a mapping from input tensor name to the input tensor value.
    # ex) "Placeholder:0" -> [0, 1, 2]
    feed_dict = _create_feed_dict_from_input_data(sample, signature_def)
    sess.run(output_tensor_names, feed_dict=feed_dict)
