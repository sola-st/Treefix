# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/gradient_descent.py
super(SGD, self)._prepare_local(var_device, var_dtype, apply_state)
apply_state[(var_device, var_dtype)]["momentum"] = array_ops.identity(
    self._get_hyper("momentum", var_dtype))
