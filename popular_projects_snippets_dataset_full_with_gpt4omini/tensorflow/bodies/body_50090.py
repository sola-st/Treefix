# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adamax.py
super(Adamax, self)._prepare_local(var_device, var_dtype, apply_state)

local_step = math_ops.cast(self.iterations + 1, var_dtype)
beta_1_t = array_ops.identity(self._get_hyper('beta_1', var_dtype))
beta_2_t = array_ops.identity(self._get_hyper('beta_2', var_dtype))
beta_1_power = math_ops.pow(beta_1_t, local_step)
lr_t = apply_state[(var_device, var_dtype)]['lr_t']

apply_state[(var_device, var_dtype)].update(
    dict(
        neg_scaled_lr=-lr_t / (1 - beta_1_power),
        epsilon=ops.convert_to_tensor_v2_with_dispatch(
            self.epsilon, var_dtype),
        beta_1_t=beta_1_t,
        beta_1_power=beta_1_power,
        one_minus_beta_1_t=1 - beta_1_t,
        beta_2_t=beta_2_t,
        zero=array_ops.zeros((), dtype=dtypes.int64)))
