# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/rmsprop.py
super(RMSprop, self)._prepare_local(var_device, var_dtype, apply_state)

rho = array_ops.identity(self._get_hyper("rho", var_dtype))
apply_state[(var_device, var_dtype)].update(
    dict(
        neg_lr_t=-apply_state[(var_device, var_dtype)]["lr_t"],
        epsilon=ops.convert_to_tensor_v2_with_dispatch(
            self.epsilon, var_dtype),
        rho=rho,
        momentum=array_ops.identity(self._get_hyper("momentum", var_dtype)),
        one_minus_rho=1. - rho))
