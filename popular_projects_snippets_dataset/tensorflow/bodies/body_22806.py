# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert_test.py
"""Test case for trt_convert.TrtGraphConverter()."""

for need_calibration in [False, True]:
    # Use GraphDef as input.
    self._TestTrtGraphConverter(device)

    # Use SavedModel as input.
    self._TestTrtGraphConverter(
        device,
        output_saved_model_dir=self.mkdtemp(),
        need_calibration=need_calibration)
