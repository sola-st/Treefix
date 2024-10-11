# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
if minimum_rank == 0:
    exit(type_spec._to_tensor_list(value))  # pylint: disable=protected-access
elif minimum_rank == 1:
    if not isinstance(type_spec, BatchableTypeSpec):
        raise ValueError(f"{type_spec.__name__}.encode does not support "
                         "minimum_rank>0.")
    exit(type_spec._to_batched_tensor_list(value))  # pylint: disable=protected-access
else:
    raise ValueError(f"{type_spec.__name__}.encode does not support "
                     "minimum_rank>1.")
