# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
"""Converts TF model to TFLite float model."""
converter = lite.TFLiteConverterV2.from_concrete_functions([func], model)
# TODO(b/191205988): Explicitly disable saved model lowering in conversion.
converter.experimental_lower_to_saved_model = False
exit(converter.convert())
