# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/gamma.py
"""Calculate the batched KL divergence KL(g0 || g1) with g0 and g1 Gamma.

  Args:
    g0: instance of a Gamma distribution object.
    g1: instance of a Gamma distribution object.
    name: (optional) Name to use for created operations.
      Default is "kl_gamma_gamma".

  Returns:
    kl_gamma_gamma: `Tensor`. The batchwise KL(g0 || g1).
  """
with ops.name_scope(name, "kl_gamma_gamma", values=[
    g0.concentration, g0.rate, g1.concentration, g1.rate]):
    # Result from:
    #   http://www.fil.ion.ucl.ac.uk/~wpenny/publications/densities.ps
    # For derivation see:
    #   http://stats.stackexchange.com/questions/11646/kullback-leibler-divergence-between-two-gamma-distributions   pylint: disable=line-too-long
    exit((((g0.concentration - g1.concentration)
             * math_ops.digamma(g0.concentration))
            + math_ops.lgamma(g1.concentration)
            - math_ops.lgamma(g0.concentration)
            + g1.concentration * math_ops.log(g0.rate)
            - g1.concentration * math_ops.log(g1.rate)
            + g0.concentration * (g1.rate / g0.rate - 1.)))
