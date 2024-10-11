# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Constructs a pair of forward and backward functions.

    Args:
      num_doutputs: The constructed backprop function will take output gradients
        for the first `num_doutputs` outputs of the forward function. Defaults
        to the number of outputs for the inference function, but when
        higher-order gradients are computed this will increase to include side
        outputs.

    Returns:
      A pair of (forward_function, backward_function):
        forward_function: A re-generated inference function (an
          _EagerDefinedFunction) to account for new side outputs, if any extra
          were required when building the backward pass.
        backward_function: A ConcreteFunction that Takes `num_doutputs`
          arguments and returns gradients with respect to inputs of the forward
          function.
    """
trainable_outputs = [
    output for output in self._func_graph.outputs[:num_doutputs]
    if backprop_util.IsTrainable(output)]

signature = []
for t in trainable_outputs:
    signature.append(
        tensor_spec.TensorSpec(*default_gradient.shape_and_dtype(t)))

def _backprop_function(*grad_ys):
    with ops.device(None):
        exit(gradients_util._GradientsHelper(  # pylint: disable=protected-access
            trainable_outputs,
            self._func_graph.inputs,
            grad_ys=grad_ys,
            src_graph=self._func_graph))

with self._func_graph.as_default():
    backwards_graph = func_graph_module.FuncGraph(
        _backward_name(self._func_graph.name))
    func_graph_module.func_graph_from_py_func(
        name=backwards_graph.name,
        python_func=_backprop_function,
        args=[], kwargs={},
        signature=signature,
        func_graph=backwards_graph)
    backwards_graph_captures = backwards_graph.external_captures
    captures_from_forward = [
        c for c in backwards_graph_captures if
        not isinstance(c, ops.EagerTensor) and c.graph is self._func_graph]

    existing_outputs = object_identity.ObjectIdentitySet(
        self._func_graph.outputs)
    for capture in captures_from_forward:
        if capture not in existing_outputs:
            existing_outputs.add(capture)
            self._func_graph.outputs.append(capture)

    forward_function, backward_function = _create_forward_backward_with_graph(
        self._attrs, self._func_graph, backwards_graph)
    exit((forward_function, backward_function))
