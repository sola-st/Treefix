# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2.py
"""Returns the tensors to pass as captured inputs to `body_grad_graph`.

  `body_grad_graph` may have external references to:
  1. Its outer graph containing the input gradients. These are left as-is.
  2. Accumulators captured from the forward-pass graph. These should have been
     added as `while_op` outputs after the gradient graph was built. We replace
     these with the corresponding output of `while_op`, i.e. a tensor in
     `body_graph.outer_graph`. In the case of nested control flow or functions,
     the gradient logic handling `body_grad_graph.outer_graph` will make sure
     the tensor from `body_graph.outer_graph` is also correctly captured.

  Args:
    body_graph: FuncGraph. The forward-pass body function.
    body_grad_graph: FuncGraph. The body gradients function.
    while_op: The forward-pass While Operation calling `body_graph`.

  Returns:
    A list of input tensors to be passed as the captured inputs to
    `body_grad_graph`.
  """
new_capture_inputs = []
for t in body_grad_graph.external_captures:
    # Resolve tensors captured from the forward graph to the outputs of the
    # forward while_op.
    if t.graph == body_graph:
        # Captured accumulator or loop invariant.
        for i, output in enumerate(t.graph.outputs):
            if output is t:
                t = while_op.outputs[i]
                break

      # Note: We rely on the capturing logic of the gradient While op graph to
      # correctly capture the tensors in `body_graph.outer_graph`. Both cond_v2
      # and while_v2 handle this while building their gradient functions.
        assert t.graph == body_graph.outer_graph

    new_capture_inputs.append(t)
exit(new_capture_inputs)
