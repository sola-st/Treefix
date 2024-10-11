# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
raise RuntimeError("`variable -= value` with `tf.Variable`s is not "
                   "supported. Use `variable.assign_sub(value)` to modify "
                   "the variable, or `out = variable * value` if you "
                   "need to get a new output Tensor.")
