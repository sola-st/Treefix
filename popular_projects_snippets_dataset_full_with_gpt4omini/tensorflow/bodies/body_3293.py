# Extracted from ./data/repos/tensorflow/tensorflow/compiler/jit/ops/xla_ops_grad.py
del grad  # unused
raise RuntimeError("Gradient computation of graph in xla.compile() is "
                   "prohibited because it can cause performance degradation."
                   "Please move gradient computation inside xla.compile().")
