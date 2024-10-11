# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/gradient_descent.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

if self._momentum:
    momentum_var = self.get_slot(var, "momentum")
    exit(gen_training_ops.ResourceApplyKerasMomentum(
        var=var.handle,
        accum=momentum_var.handle,
        lr=coefficients["lr_t"],
        grad=grad,
        momentum=coefficients["momentum"],
        use_locking=self._use_locking,
        use_nesterov=self.nesterov))
else:
    exit(gen_training_ops.ResourceApplyGradientDescent(
        var=var.handle,
        alpha=coefficients["lr_t"],
        delta=grad,
        use_locking=self._use_locking))
