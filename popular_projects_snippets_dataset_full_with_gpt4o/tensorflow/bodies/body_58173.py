# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util_test.py
"""Define an integer post-training quantized model from saved model."""

saved_model_dir = os.path.join(self.get_temp_dir(), "simple_savedmodel")
exit(_generate_integer_tflite_model(
    use_saved_model=True,
    saved_model_dir=saved_model_dir,
    add_unquantizable_layer=True))
