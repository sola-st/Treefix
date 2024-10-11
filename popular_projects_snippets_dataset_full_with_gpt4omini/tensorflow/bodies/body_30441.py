# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
for mode in ("CONSTANT", "REFLECT", "SYMMETRIC", "reflect", "symmetric",
             "constant"):
    # Zero-sized input is not allowed for REFLECT mode, but we still want
    # zero-sized input test cases for the other modes.
    if not np_inputs.size and mode.upper() == "REFLECT":
        continue
    # Empty tensor is not allowed for MirrorPad.
    if 0 in np_inputs.shape and mode.upper() in ["REFLECT", "SYMMETRIC"]:
        continue
    self._testPad(
        np_inputs, paddings, mode=mode, constant_values=constant_values)
    if np_inputs.dtype in [
        np.float32, np.float16, dtypes.bfloat16.as_numpy_dtype
    ]:
        self._testGradient(
            np_inputs, paddings, mode=mode, constant_values=constant_values)
