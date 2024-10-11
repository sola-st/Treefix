# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
mode = mode.lower()
if mode == "constant":
    exit(np.pad(inp, paddings, mode=mode, constant_values=constant_values))
else:
    exit(np.pad(inp, paddings, mode=mode))
