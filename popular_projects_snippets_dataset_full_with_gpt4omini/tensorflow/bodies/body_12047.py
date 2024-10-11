# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
raise LookupError("Gradient explicitly disabled. Reason: %s" %
                  op.get_attr("message"))
