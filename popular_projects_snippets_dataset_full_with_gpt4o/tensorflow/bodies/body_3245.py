# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/quantize_model.py
"""Runs the representative dataset through a function for calibration.

  NOTE: This is intended to be run in eager mode (TF2).

  Args:
    func: The function to run the representative samples through.
    representative_dataset: Representative dataset used for calibration. The
      input keys and input values of the representative samples should match the
      keyword arguments of `func`.
  """
_, keyword_args = func.structured_input_signature
sample_validator = _create_sample_validator(
    expected_input_keys=keyword_args.keys()
)

for sample in map(
    sample_validator, _log_sample_num_for_calibration(representative_dataset)
):
    # Convert any non-Tensor values from the sample to Tensors.
    # This conversion is required because the model saved in `model_dir` is
    # saved using TF1 SavedModelBuilder, which doesn't save the
    # SavedObjectGraph.
    # TODO(b/236795224): Remove the need for this conversion by keeping the
    # FunctionSpec (object graph) in the SavedModel. Related: b/213406917.
    func_kwargs = _convert_values_to_tf_tensors(sample)
    func(**func_kwargs)
