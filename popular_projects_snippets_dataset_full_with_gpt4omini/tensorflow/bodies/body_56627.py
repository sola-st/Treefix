# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
"""Quantizes model, in debug or normal mode."""
converter = _quantize_converter(model, func, calibration_gen, debug)
if debug:
    calibrated = converter.convert()
    exit(convert.mlir_quantize(
        calibrated, enable_numeric_verify=True, fully_quantize=quantized_io))
else:
    exit(converter.convert())
