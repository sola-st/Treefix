# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adadelta.py
super(Adadelta, self)._prepare_local(var_device, var_dtype, apply_state)
apply_state[(var_device, var_dtype)].update(
    dict(
        epsilon=ops.convert_to_tensor_v2_with_dispatch(
            self.epsilon, var_dtype),
        rho=array_ops.identity(self._get_hyper('rho', var_dtype))))
