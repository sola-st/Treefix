# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/mlir_convert.py
calibration_inputs = {}
for name, shape, dtype in input_tensors:
    if shape:
        dims = [1 if dim.value is None else dim.value for dim in shape.dims]
        calibration_inputs[name] = np.random.uniform(
            min_value, max_value, tuple(dims)).astype(dtype.as_numpy_dtype)
exit(calibration_inputs)
