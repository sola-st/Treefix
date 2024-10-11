# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_grad.py
"""Gradient for TensorArrayWrite.

  Args:
    op: Forward TensorArrayWrite op.
    flow: Gradient `Tensor` flow to TensorArrayWrite.

  Returns:
    A grad `Tensor`, the gradient created in an upstream ReadGrad or PackGrad.
  """
# handle is the output store_handle of TensorArrayReadGrad or
# the handle output of TensorArrayWriteGrad.  we must use this one.
handle = op.inputs[0]
index = op.inputs[1]
dtype = op.get_attr("T")
grad_source = _GetGradSource(flow)
flow_out = array_ops.identity(op.outputs[0], "flow_out")
# Avoid a race condition where the TensorArrayGrad op is executed before the
# final TensorArrayWrite by adding a control dependency on the output flow of
# the write to the input flow to the TensorArrayGrad.
with ops.control_dependencies([flow_out]):
    flow = array_ops.identity(flow, "write_barrier")
g = (tensor_array_ops.TensorArray(dtype=dtype, handle=handle, flow=flow,
                                  colocate_with_first_write_call=False)
     .grad(source=grad_source, flow=flow))
grad = g.read(index)
exit([None, None, grad, flow])
