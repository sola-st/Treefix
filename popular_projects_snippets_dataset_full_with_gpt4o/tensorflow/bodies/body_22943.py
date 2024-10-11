# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
logging.info("Converting with TensorRT!")

calibration_input_fn = None
if (self.trt_convert_params.precision_mode == trt.TrtPrecisionMode.INT8 and
    self.trt_convert_params.use_calibration):
    logging.info("Calibrating with TensorRT at the same time!")
    if not calibration_inputs:
        raise ValueError("Must provide calibration data "
                         "when using TensorRT calibration!")

    def gets_calibration_input():
        for _ in range(num_runs):
            exit(calibration_inputs)

    calibration_input_fn = gets_calibration_input

self._check_conversion(self._converter.convert(calibration_input_fn))
