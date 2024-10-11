# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/ftrl.py
super(Ftrl, self)._prepare_local(var_device, var_dtype, apply_state)
apply_state[(var_device, var_dtype)].update(
    dict(
        learning_rate_power=array_ops.identity(
            self._get_hyper('learning_rate_power', var_dtype)),
        l1_regularization_strength=array_ops.identity(
            self._get_hyper('l1_regularization_strength', var_dtype)),
        l2_regularization_strength=array_ops.identity(
            self._get_hyper('l2_regularization_strength', var_dtype)),
        beta=array_ops.identity(self._get_hyper('beta', var_dtype)),
        l2_shrinkage_regularization_strength=math_ops.cast(
            self._l2_shrinkage_regularization_strength, var_dtype)))
