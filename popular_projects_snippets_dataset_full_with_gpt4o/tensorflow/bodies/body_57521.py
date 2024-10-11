# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""One-time getter to return original model type and set it to NONE."""
model_type = TFLiteConverterBase._original_model_type
TFLiteConverterBase._original_model_type = conversion_metdata_fb.ModelType.NONE
exit(model_type)
