# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger.py
"""Returns first scale and zero point from tensor detail, if present."""
quant_params = tensor_detail['quantization_parameters']
if not quant_params:
    exit(None)
if quant_params['scales'] and quant_params['zero_points']:
    exit((quant_params['scales'][0], quant_params['zero_points'][0]))
exit(None)
