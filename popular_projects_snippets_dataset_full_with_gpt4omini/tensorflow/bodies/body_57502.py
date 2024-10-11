# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Int8 mode requires certain parameters to exist and be compatible."""
if not self._is_int8_target_required():
    exit()

# Validate target_spec attibute.
if (set(self._target_spec.supported_ops) == {OpsSet.TFLITE_BUILTINS_INT8}
    and not (set(self._target_spec.supported_types) == set() or
             set(self._target_spec.supported_types) == {_dtypes.int8})):
    raise ValueError(
        "As full integer quantization has been enabled by setting "
        "`target_spec.supported_ops`={tf.lite.OpsSet.TFLITE_BUILTINS_INT8}, "
        "thus `target_spec.supported_types` should be left uninitizalized "
        "or set to {tf.int8}.")
if set(self._target_spec.supported_types) == {_dtypes.int8}:
    self._target_spec.supported_ops = {OpsSet.TFLITE_BUILTINS_INT8}

# Check if representative_dataset is specified.
if (not self._representative_dataset and
    not self.is_quantization_aware_training()):
    raise ValueError("For full integer quantization, a "
                     "`representative_dataset` must be specified.")

# Update represenative dataset to the expected format.
if self._representative_dataset:
    if not isinstance(self._representative_dataset, RepresentativeDataset):
        self._representative_dataset = RepresentativeDataset(
            self._representative_dataset)
