# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Stores the original model type."""
if model_type == conversion_metdata_fb.ModelType.NONE:
    raise ValueError("The original model type should be specified.")
cls._original_model_type = model_type
