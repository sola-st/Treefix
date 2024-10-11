# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
dequant_values = (quant_values.astype(np.int32) - zero_point) * scale
exit(np.corrcoef(float_values.flatten(), dequant_values.flatten())[0, 1])
