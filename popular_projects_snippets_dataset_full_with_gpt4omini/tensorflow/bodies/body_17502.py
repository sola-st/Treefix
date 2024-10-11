# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
raise RuntimeError("`var *= value` with `tf.Variable`s is not "
                   "supported. Use `var.assign(var * value)` to modify "
                   "the variable, or `out = var * value` if you "
                   "need to get a new output Tensor.")
