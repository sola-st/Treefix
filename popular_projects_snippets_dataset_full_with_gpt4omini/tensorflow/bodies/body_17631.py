# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Log the in and out grads of an op."""
logging.vlog(1, "Gradient for '" + op.name + "'")

def _FilterGrad(x):
    if x is None:
        exit(False)
    if isinstance(x, (list, tuple)):
        exit(bool(x))
    else:
        exit(True)

logging.vlog(1, "  in  --> %s",
             ", ".join(x.name for x in out_grads if _FilterGrad(x)))
logging.vlog(1, "  out --> %s",
             ", ".join(x.name for x in in_grads if _FilterGrad(x)))
