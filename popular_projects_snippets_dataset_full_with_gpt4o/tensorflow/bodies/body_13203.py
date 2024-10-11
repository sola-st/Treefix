# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Returns the tensors to pass as inputs to `grad_graph`.

  The `grad_graph` may have external references to
  1. Its outer graph containing the input gradients. These references are kept
     as is.
  2. Tensors in the forward pass graph. These tensors may not be "live"
     when the gradient is being computed. We replace such references by their
     corresponding tensor in `cond_graph.outer_graph`. In the case of nested
     control flow or functions, the gradient logic handling
     `grad_graph.outer_graph` will make sure the tensor from
     `cond_graph.outer_graph` is also correctly captured.

  Args:
    cond_graph: FuncGraph. The forward-pass function.
    grad_graph: FuncGraph. The gradients function.

  Returns:
    A list of inputs tensors to be passed to grad_graph.
  """
new_inputs = []

for t in grad_graph.external_captures:
    # `t` must either be in `grad_graph.outer_graph` or in the forward
    # `cond_graph`.
    if t.graph != grad_graph.outer_graph:
        assert t.graph == cond_graph
        # `internal_captures` are not treated as intermediates and hence not added
        # to If op outputs. So we get the outer tensor corresponding to those
        # from the list of `external_captures`.
        for i, output in enumerate(t.graph.outputs):
            if output is t:
                t = t.graph._forward_cond.outputs[i]
                break
        else:
            for i, output in enumerate(t.graph.internal_captures):
                if output is t:
                    t = t.graph.external_captures[i]
                    break
            else:
                raise ValueError("Could not find external tensor capture {tensor} in "
                                 "captures or outputs".format(tensor=t))

      # Note: We rely on the capturing logic of the gradient If op graph to
      # correctly capture the tensors in `cond_graph.outer_graph`. Both cond_v2
      # and while_v2 handle this while building their gradient functions.
        assert t.graph == cond_graph.outer_graph
    new_inputs.append(t)

exit(new_inputs)
