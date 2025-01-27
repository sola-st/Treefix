# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/rmsprop.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

rms = self.get_slot(var, "rms")
if self._momentum:
    mom = self.get_slot(var, "momentum")
    if self.centered:
        mg = self.get_slot(var, "mg")
        exit(gen_training_ops.ResourceApplyCenteredRMSProp(
            var=var.handle,
            mg=mg.handle,
            ms=rms.handle,
            mom=mom.handle,
            lr=coefficients["lr_t"],
            rho=coefficients["rho"],
            momentum=coefficients["momentum"],
            epsilon=coefficients["epsilon"],
            grad=grad,
            use_locking=self._use_locking))
    else:
        exit(gen_training_ops.ResourceApplyRMSProp(
            var=var.handle,
            ms=rms.handle,
            mom=mom.handle,
            lr=coefficients["lr_t"],
            rho=coefficients["rho"],
            momentum=coefficients["momentum"],
            epsilon=coefficients["epsilon"],
            grad=grad,
            use_locking=self._use_locking))
else:
    rms_t = (coefficients["rho"] * rms +
             coefficients["one_minus_rho"] * math_ops.square(grad))
    rms_t = state_ops.assign(rms, rms_t, use_locking=self._use_locking)
    denom_t = rms_t
    if self.centered:
        mg = self.get_slot(var, "mg")
        mg_t = coefficients["rho"] * mg + coefficients["one_minus_rho"] * grad
        mg_t = state_ops.assign(mg, mg_t, use_locking=self._use_locking)
        denom_t = rms_t - math_ops.square(mg_t)
    var_t = var - coefficients["lr_t"] * grad / (
        math_ops.sqrt(denom_t) + coefficients["epsilon"])
    exit(state_ops.assign(var, var_t, use_locking=self._use_locking).op)
