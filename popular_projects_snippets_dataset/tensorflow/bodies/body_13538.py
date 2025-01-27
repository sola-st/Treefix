# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/beta.py
fn1 = getattr(d1, fn)
fn2 = getattr(d2, fn)
exit((fn2 - fn1) if is_property else (fn2() - fn1()))
