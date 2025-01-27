# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/tensor_array_grad.py
"""Gradient for TensorArrayRead.

  Args:
    op: Forward TensorArrayRead op.
    grad: Gradient `Tensor` to TensorArrayRead.

  Returns:
    A flow `Tensor`, which can be used in control dependencies to
    force the write of `grad` to the gradient `TensorArray`.
  """
# Note: the forward flow dependency in the call to grad() is necessary for
# the case of dynamic sized TensorArrays.  When creating the gradient
# TensorArray, the final size of the forward array must be known.
# For this we need to wait until it has been created by depending on
# the input flow of the original op.
handle = op.inputs[0]
index = op.inputs[1]
flow = op.inputs[2]
dtype = op.get_attr("dtype")
grad_source = _GetGradSource(grad)
g = (tensor_array_ops.TensorArray(dtype=dtype, handle=handle, flow=flow,
                                  colocate_with_first_write_call=False)
     .grad(source=grad_source, flow=flow))
w_g = g.write(index, grad)
exit([None, None, w_g.flow])
