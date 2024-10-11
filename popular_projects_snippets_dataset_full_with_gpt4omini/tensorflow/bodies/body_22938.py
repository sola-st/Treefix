# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/model_tests/model_handler.py
logging.info("Converting with TensorRT!")
self._check_conversion(self._converter.convert())

if (self.trt_convert_params.precision_mode == trt.TrtPrecisionMode.INT8 and
    self.trt_convert_params.use_calibration):
    logging.info("Calibrating with TensorRT!")
    if not calibration_inputs:
        raise ValueError("Must provide calibration data "
                         "when using TensorRT calibration!")
    try:
        self._converter.calibrate(
            fetch_names=self.output_tensor_names,
            num_runs=num_runs,
            feed_dict_fn=lambda: calibration_inputs)
    except Exception as exc:
        raise RuntimeError("Failed to calibrate! "
                           "Model Information: {}".format(str(self))) from exc
