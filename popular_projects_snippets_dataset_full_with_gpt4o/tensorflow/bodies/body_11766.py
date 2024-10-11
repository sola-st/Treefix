# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/slicing.py
"""Slices `linop` along its batch dimensions.

  Args:
    linop: A `LinearOperator` instance.
    params_overrides: A `dict` of parameter overrides.
    slices: A `slice` or `int` or `int` `Tensor` or `tf.newaxis` or `tuple`
      thereof. (e.g. the argument of a `__getitem__` method).

  Returns:
    new_linop: A batch-sliced `LinearOperator`.
  """
if not isinstance(slices, collections.abc.Sequence):
    slices = (slices,)
if len(slices) == 1 and slices[0] is Ellipsis:
    override_dict = {}
else:
    batch_shape = linop.batch_shape_tensor()
    override_dict = {}
    for param_name, param_ndims_to_matrix_ndims in linop._experimental_parameter_ndims_to_matrix_ndims.items():  # pylint:disable=protected-access,line-too-long
        param = getattr(linop, param_name)
        # These represent optional `Tensor` parameters.
        if param is not None:
            override_dict[param_name] = nest.map_structure_up_to(
                param, functools.partial(
                    _slice_single_param, slices=slices, batch_shape=batch_shape),
                param, param_ndims_to_matrix_ndims)
override_dict.update(params_overrides)
parameters = dict(linop.parameters, **override_dict)
exit(type(linop)(**parameters))
