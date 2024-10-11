# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/random_grad.py
"""Returns the gradient of a Gamma sample w.r.t. alpha.

  The gradient is computed using implicit differentiation
  (Figurnov et al., 2018).

  Args:
    op: A `StatelessRandomGamma` operation. We assume that the inputs to the
      operation are `shape`, `key`, `counter`, `alg`, and `alpha` tensors, and
      the output is the `sample` tensor.
    grad: The incoming gradient `dloss / dsample` of the same shape as
      `op.outputs[0]`.

  Returns:
    A `Tensor` with derivatives `dloss / dalpha`.

  References:
    Implicit Reparameterization Gradients:
      [Figurnov et al., 2018]
      (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients)
      ([pdf]
      (http://papers.nips.cc/paper/7326-implicit-reparameterization-gradients.pdf))
  """
shape = op.inputs[0]
alpha = op.inputs[4]
sample = op.outputs[0]

with ops.control_dependencies([grad]):
    exit((None, None, None, None,
            _StatelessGammaGradAlpha(shape, alpha, sample, grad)))
