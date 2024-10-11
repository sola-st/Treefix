# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/rmsprop.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

rms = self.get_slot(var, "rms")
if self._momentum:
    mom = self.get_slot(var, "momentum")
    if self.centered:
        mg = self.get_slot(var, "mg")
        exit(gen_training_ops.ResourceSparseApplyCenteredRMSProp(
            var=var.handle,
            mg=mg.handle,
            ms=rms.handle,
            mom=mom.handle,
            lr=coefficients["lr_t"],
            rho=coefficients["rho"],
            momentum=coefficients["momentum"],
            epsilon=coefficients["epsilon"],
            grad=grad,
            indices=indices,
            use_locking=self._use_locking))
    else:
        exit(gen_training_ops.ResourceSparseApplyRMSProp(
            var=var.handle,
            ms=rms.handle,
            mom=mom.handle,
            lr=coefficients["lr_t"],
            rho=coefficients["rho"],
            momentum=coefficients["momentum"],
            epsilon=coefficients["epsilon"],
            grad=grad,
            indices=indices,
            use_locking=self._use_locking))
else:
    rms_scaled_g_values = (grad * grad) * coefficients["one_minus_rho"]
    rms_t = state_ops.assign(rms, rms * coefficients["rho"],
                             use_locking=self._use_locking)
    with ops.control_dependencies([rms_t]):
        rms_t = self._resource_scatter_add(rms, indices, rms_scaled_g_values)
        rms_slice = array_ops.gather(rms_t, indices)
    denom_slice = rms_slice
    if self.centered:
        mg = self.get_slot(var, "mg")
        mg_scaled_g_values = grad * coefficients["one_minus_rho"]
        mg_t = state_ops.assign(mg, mg * coefficients["rho"],
                                use_locking=self._use_locking)
        with ops.control_dependencies([mg_t]):
            mg_t = self._resource_scatter_add(mg, indices, mg_scaled_g_values)
            mg_slice = array_ops.gather(mg_t, indices)
            denom_slice = rms_slice - math_ops.square(mg_slice)
    var_update = self._resource_scatter_add(
        var, indices, coefficients["neg_lr_t"] * grad / (
            math_ops.sqrt(denom_slice) + coefficients["epsilon"]))
    if self.centered:
        exit(control_flow_ops.group(*[var_update, rms_t, mg_t]))
    exit(control_flow_ops.group(*[var_update, rms_t]))
