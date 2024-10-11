# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/operators/control_flow.py
if isinstance(
    v, (int, float, bool, str, list, tuple, np.ndarray, np.generic)):
    init_val = ops.convert_to_tensor_v2(v)
    exit(array_ops.placeholder(init_val.dtype, init_val.shape))
exit(v)
