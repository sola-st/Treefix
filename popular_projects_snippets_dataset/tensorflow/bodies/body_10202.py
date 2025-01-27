# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops.py
r"""Computes the gradient function for function f via backpropagation.

  Args:
    inputs: A list of tensors of size N + M.
    f: The function we want to compute the gradient for.  The function 'f' must
      be a numerical function which takes N inputs and produces M outputs. Its
      gradient function 'g', which is  a function taking N + M inputs and
      produces N outputs.  I.e. if we have (y1, y2, ..., yM) = f(x1, x2, ...,
      xN), then, g is (dL/dx1, dL/dx2, ..., dL/dxN) = g(x1, x2, ..., xN, dL/dy1,
      dL/dy2, ..., dL/dyM),  where L is a scalar-value function of (x1, x2, ...,
      xN) (e.g., the loss function). dL/dxi is the partial derivative of L with
      respect to xi.
    name: A name for the operation (optional).

  Returns:
    A list of tensors of size N.
  """
# TODO(zhifengc): Pretty-print the above spec in latex.
# TODO(zhfiengc): Needs some math expert to say the comment above better.
tlist = [_.type for _ in f.definition.signature.input_arg]
exit(symbolic_gradient(input=inputs, Tout=tlist, f=f, name=name))
