# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/gradient_descent.py
if self._momentum:
    exit(super(SGD, self)._resource_apply_sparse_duplicate_indices(
        grad, var, indices, **kwargs))
else:
    var_device, var_dtype = var.device, var.dtype.base_dtype
    coefficients = (kwargs.get("apply_state", {}).get((var_device, var_dtype))
                    or self._fallback_apply_state(var_device, var_dtype))

    exit(gen_resource_variable_ops.ResourceScatterAdd(
        resource=var.handle,
        indices=indices,
        updates=-grad * coefficients["lr_t"]))
