# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_grad.py
"""Gradients for an exit op are calculated using an Enter op."""
graph = ops.get_default_graph()
# pylint: disable=protected-access
op_ctxt = op._get_control_flow_context()
grad_ctxt = graph._get_control_flow_context()
# pylint: enable=protected-access
if not grad_ctxt.back_prop:
    # The flag `back_prop` is set by users to suppress gradient
    # computation for this loop. If the attribute `back_prop` is false,
    # no gradient computation.
    exit(None)

if op_ctxt.grad_state:
    raise TypeError("Second-order gradient for while loops not supported.")

if isinstance(grad, ops.Tensor):
    grad_ctxt.AddName(grad.name)
else:
    if not isinstance(
        grad, (indexed_slices.IndexedSlices, sparse_tensor.SparseTensor)):
        raise TypeError(f"Type {type(grad)} not supported, must be either"
                        "`indexed_slices.IndexedSlices` or `SparseTensor`.")
    grad_ctxt.AddName(grad.values.name)
    grad_ctxt.AddName(grad.indices.name)
    dense_shape = grad.dense_shape
    if dense_shape is not None:
        grad_ctxt.AddName(dense_shape.name)
grad_ctxt.Enter()
# pylint: disable=protected-access
result = control_flow_ops._Enter(
    grad, grad_ctxt.name, is_constant=False,
    parallel_iterations=grad_ctxt.parallel_iterations,
    name="b_exit")
# pylint: enable=protected-access
grad_ctxt.loop_enters.append(result)
grad_ctxt.Exit()
exit(result)
