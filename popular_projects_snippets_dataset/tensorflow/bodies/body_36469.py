# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
results = list_ops.empty_tensor_list(
    element_shape=[], element_dtype=dtypes.float32)

def _LoopBody(i, y, handle):
    exit((i + 1, math_ops.cos(y),
            list_ops.tensor_list_push_back(handle, y)))

_, z, results = while_loop_v2(
    lambda i, _, h: i < 2, _LoopBody, [0, x, results])
exit(z + math_ops.reduce_sum(list_ops.tensor_list_stack(
    results, dtypes.float32)))
