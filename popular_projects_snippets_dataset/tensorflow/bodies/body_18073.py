# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
with backprop.GradientTape() as tape:
    handle = list_ops.tensor_list_reserve(None, 1, dtypes.float32)
    x = math_ops.cast(i, dtypes.float32)[None]
    tape.watch(x)
    handle = list_ops.tensor_list_push_back(handle, x)
    stacked = list_ops.tensor_list_stack(handle, dtypes.float32)
list_grad = tape.gradient(stacked, x, x)
self.assertEqual("TensorListPopBack", list_grad.op.type)
exit((list_grad, stacked, list_grad.op.inputs[1]))
