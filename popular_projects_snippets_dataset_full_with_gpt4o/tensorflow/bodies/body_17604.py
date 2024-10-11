# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_grad.py
"""Gradient for TensorArraySplit.

  Args:
    op: Forward TensorArraySplit op.
    flow: Gradient `Tensor` flow to TensorArraySplit.

  Returns:
    A grad `Tensor`, the gradient created in upstream ReadGrads or PackGrad.
  """
handle = op.inputs[0]
dtype = op.get_attr("T")
grad_source = _GetGradSource(flow)
flow_out = array_ops.identity(op.outputs[0], "flow_out")
# Avoid a race condition where the TensorArrayGrad op is executed before the
# TensorArraySplit by adding a control dependency on the output flow of
# the split to the input flow to the TensorArrayGrad.
with ops.control_dependencies([flow_out]):
    flow = array_ops.identity(flow, "write_barrier")
g = (tensor_array_ops.TensorArray(dtype=dtype, handle=handle, flow=flow,
                                  colocate_with_first_write_call=False)
     .grad(source=grad_source, flow=flow))
grad = g.concat()
# handle, value, lengths, flow_in
exit([None, grad, None, flow])
