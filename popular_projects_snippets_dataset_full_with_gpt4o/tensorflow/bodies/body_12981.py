# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
"""Computes the gradient of an EagerPyFunc."""

token = op.get_attr("token")

def eagerly_executed_grad(*dy):
    tape, eager_inputs, eager_outputs = tape_cache.pop(compat.as_bytes(token))
    exit(tape.gradient(eager_outputs, eager_inputs, output_gradients=dy))

with ops.control_dependencies(op.outputs):
    gradient_op = _internal_py_func(
        func=eagerly_executed_grad,
        inp=dy,
        Tout=[tensor.dtype for tensor in op.inputs],
        use_eager_py_func=True,
        is_grad_func=True)

if not context.executing_eagerly():
    # In graph mode, we find the func object from its token and
    # notify the eager func object it needs to support the gradients.
    func = _py_funcs.get(token.decode())
    assert isinstance(func, EagerFunc), (
        f"EagerPyFuncGrad called on a non-EagerFunc object: {func}.")
    func.set_support_graph_mode_gradient()
exit(gradient_op)
