# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/dirichlet.py
"""Batchwise KL divergence KL(d1 || d2) with d1 and d2 Dirichlet.

  Args:
    d1: instance of a Dirichlet distribution object.
    d2: instance of a Dirichlet distribution object.
    name: (optional) Name to use for created operations.
      default is "kl_dirichlet_dirichlet".

  Returns:
    Batchwise KL(d1 || d2)
  """
with ops.name_scope(name, "kl_dirichlet_dirichlet", values=[
    d1.concentration, d2.concentration]):
    # The KL between Dirichlet distributions can be derived as follows. We have
    #
    #   Dir(x; a) = 1 / B(a) * prod_i[x[i]^(a[i] - 1)]
    #
    # where B(a) is the multivariate Beta function:
    #
    #   B(a) = Gamma(a[1]) * ... * Gamma(a[n]) / Gamma(a[1] + ... + a[n])
    #
    # The KL is
    #
    #   KL(Dir(x; a), Dir(x; b)) = E_Dir(x; a){log(Dir(x; a) / Dir(x; b))}
    #
    # so we'll need to know the log density of the Dirichlet. This is
    #
    #   log(Dir(x; a)) = sum_i[(a[i] - 1) log(x[i])] - log B(a)
    #
    # The only term that matters for the expectations is the log(x[i]). To
    # compute the expectation of this term over the Dirichlet density, we can
    # use the following facts about the Dirichlet in exponential family form:
    #   1. log(x[i]) is a sufficient statistic
    #   2. expected sufficient statistics (of any exp family distribution) are
    #      equal to derivatives of the log normalizer with respect to
    #      corresponding natural parameters: E{T[i](x)} = dA/d(eta[i])
    #
    # To proceed, we can rewrite the Dirichlet density in exponential family
    # form as follows:
    #
    #   Dir(x; a) = exp{eta(a) . T(x) - A(a)}
    #
    # where '.' is the dot product of vectors eta and T, and A is a scalar:
    #
    #   eta[i](a) = a[i] - 1
    #     T[i](x) = log(x[i])
    #        A(a) = log B(a)
    #
    # Now, we can use fact (2) above to write
    #
    #   E_Dir(x; a)[log(x[i])]
    #       = dA(a) / da[i]
    #       = d/da[i] log B(a)
    #       = d/da[i] (sum_j lgamma(a[j])) - lgamma(sum_j a[j])
    #       = digamma(a[i])) - digamma(sum_j a[j])
    #
    # Putting it all together, we have
    #
    # KL[Dir(x; a) || Dir(x; b)]
    #     = E_Dir(x; a){log(Dir(x; a) / Dir(x; b)}
    #     = E_Dir(x; a){sum_i[(a[i] - b[i]) log(x[i])} - (lbeta(a) - lbeta(b))
    #     = sum_i[(a[i] - b[i]) * E_Dir(x; a){log(x[i])}] - lbeta(a) + lbeta(b)
    #     = sum_i[(a[i] - b[i]) * (digamma(a[i]) - digamma(sum_j a[j]))]
    #          - lbeta(a) + lbeta(b))

    digamma_sum_d1 = math_ops.digamma(
        math_ops.reduce_sum(d1.concentration, axis=-1, keepdims=True))
    digamma_diff = math_ops.digamma(d1.concentration) - digamma_sum_d1
    concentration_diff = d1.concentration - d2.concentration

    exit((math_ops.reduce_sum(concentration_diff * digamma_diff, axis=-1) -
            special_math_ops.lbeta(d1.concentration) +
            special_math_ops.lbeta(d2.concentration)))
