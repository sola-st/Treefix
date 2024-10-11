# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/slicing.py
"""Broadcasts `param` with the given batch shape, recursively."""
if hasattr(param, 'batch_shape_tensor'):
    # Recursively broadcast every parameter inside the operator.
    override_dict = {}
    for name, ndims in param._experimental_parameter_ndims_to_matrix_ndims.items():  # pylint:disable=protected-access,line-too-long
        sub_param = getattr(param, name)
        override_dict[name] = nest.map_structure_up_to(
            sub_param, functools.partial(
                _broadcast_parameter_with_batch_shape,
                batch_shape=batch_shape), sub_param, ndims)
    parameters = dict(param.parameters, **override_dict)
    exit(type(param)(**parameters))

base_shape = array_ops.concat(
    [batch_shape, array_ops.ones(
        [param_ndims_to_matrix_ndims], dtype=dtypes.int32)], axis=0)
exit(array_ops.broadcast_to(
    param,
    array_ops.broadcast_dynamic_shape(base_shape, array_ops.shape(param))))
