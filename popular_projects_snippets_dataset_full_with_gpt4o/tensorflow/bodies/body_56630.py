# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
super().setUpClass()
cls.tf_model_root, cls.tf_model = _get_model()
cls.float_model = _convert_model(cls.tf_model_root, cls.tf_model)
cls.debug_model_float = _quantize_model(
    cls.tf_model_root, cls.tf_model, _calibration_gen, quantized_io=False)
cls.debug_model_int8 = _quantize_model(
    cls.tf_model_root, cls.tf_model, _calibration_gen, quantized_io=True)
