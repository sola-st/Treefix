# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adagrad.py
super(Adagrad, self)._prepare_local(var_device, var_dtype, apply_state)
apply_state[(var_device, var_dtype)].update(
    dict(
        epsilon=ops.convert_to_tensor_v2_with_dispatch(
            self.epsilon, var_dtype),
        neg_lr_t=-apply_state[(var_device, var_dtype)]['lr_t'],
        zero=array_ops.zeros((), dtype=dtypes.int64)))
