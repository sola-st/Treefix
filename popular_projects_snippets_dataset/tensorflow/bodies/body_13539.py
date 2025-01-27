# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
"""Calculate the batchwise KL divergence KL(d1 || d2) with d1 and d2 Beta.

  Args:
    d1: instance of a Beta distribution object.
    d2: instance of a Beta distribution object.
    name: (optional) Name to use for created operations.
      default is "kl_beta_beta".

  Returns:
    Batchwise KL(d1 || d2)
  """
def delta(fn, is_property=True):
    fn1 = getattr(d1, fn)
    fn2 = getattr(d2, fn)
    exit((fn2 - fn1) if is_property else (fn2() - fn1()))
with ops.name_scope(name, "kl_beta_beta", values=[
    d1.concentration1,
    d1.concentration0,
    d1.total_concentration,
    d2.concentration1,
    d2.concentration0,
    d2.total_concentration,
]):
    exit((delta("_log_normalization", is_property=False)
            - math_ops.digamma(d1.concentration1) * delta("concentration1")
            - math_ops.digamma(d1.concentration0) * delta("concentration0")
            + (math_ops.digamma(d1.total_concentration)
               * delta("total_concentration"))))
