# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Quantize the model."""
# pylint: disable=protected-access
custom_op_registerers_by_name = [
    x for x in self.target_spec._experimental_custom_op_registerers
    if isinstance(x, str)
]
custom_op_registerers_by_func = [
    x for x in self.target_spec._experimental_custom_op_registerers
    if not isinstance(x, str)
]
# pylint: enable=protected-access
if not isinstance(self.representative_dataset, RepresentativeDataset):
    self.representative_dataset = RepresentativeDataset(
        self.representative_dataset)

# Add intermediate tensors to the model if needed.
result = _calibrator.add_intermediate_tensors(result)
calibrate_quantize = _calibrator.Calibrator(result,
                                            custom_op_registerers_by_name,
                                            custom_op_registerers_by_func)
if self._experimental_calibrate_only or self.experimental_new_quantizer:
    calibrated = calibrate_quantize.calibrate(
        self.representative_dataset.input_gen)

if self._experimental_calibrate_only:
    exit(calibrated)
elif self.experimental_new_quantizer and (
    activations_type != _dtypes.int16):
    # TODO(b/175659372): remove the activations_type restriction and enable
    # it for all the activation types.
    exit(_mlir_quantize(
        calibrated,
        self._experimental_disable_per_channel,
        input_data_type=input_type,
        output_data_type=output_type,
        enable_variable_quantization=enable_variable_quantization))
else:
    exit(calibrate_quantize.calibrate_and_quantize(
        self.representative_dataset.input_gen,
        input_type,
        output_type,
        allow_float,
        activations_type,
        bias_type,
        disable_per_channel=self._experimental_disable_per_channel))
