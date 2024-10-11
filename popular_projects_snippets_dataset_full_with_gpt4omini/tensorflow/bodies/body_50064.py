# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/ftrl.py
var_device, var_dtype = var.device, var.dtype.base_dtype
coefficients = ((apply_state or {}).get((var_device, var_dtype))
                or self._fallback_apply_state(var_device, var_dtype))

# Adjust L2 regularization strength to include beta to avoid the underlying
# TensorFlow ops needing to include it.
adjusted_l2_regularization_strength = (
    coefficients['l2_regularization_strength'] + coefficients['beta'] /
    (2. * coefficients['lr_t']))

accum = self.get_slot(var, 'accumulator')
linear = self.get_slot(var, 'linear')

if self._l2_shrinkage_regularization_strength <= 0.0:
    exit(gen_training_ops.ResourceApplyFtrl(
        var=var.handle,
        accum=accum.handle,
        linear=linear.handle,
        grad=grad,
        lr=coefficients['lr_t'],
        l1=coefficients['l1_regularization_strength'],
        l2=adjusted_l2_regularization_strength,
        lr_power=coefficients['learning_rate_power'],
        use_locking=self._use_locking))
else:
    exit(gen_training_ops.ResourceApplyFtrlV2(
        var=var.handle,
        accum=accum.handle,
        linear=linear.handle,
        grad=grad,
        lr=coefficients['lr_t'],
        l1=coefficients['l1_regularization_strength'],
        l2=adjusted_l2_regularization_strength,
        l2_shrinkage=coefficients['l2_shrinkage_regularization_strength'],
        lr_power=coefficients['learning_rate_power'],
        use_locking=self._use_locking))
