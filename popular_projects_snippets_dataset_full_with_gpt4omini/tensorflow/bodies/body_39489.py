# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""A pared-down version of get_variable which does not reuse variables."""
dtype = dtypes.as_dtype(dtype)
shape_object = tensor_shape.as_shape(shape)
with ops.init_scope():
    if initializer is None:
        initializer, initializing_from_value = (
            variable_scope._get_default_variable_store()._get_default_initializer(  # pylint: disable=protected-access
                name=name,
                shape=shape_object,
                dtype=dtype))
    else:
        initializing_from_value = not callable(initializer)
    # Same logic as get_variable
    variable_dtype = dtype.base_dtype
    if initializing_from_value:
        if shape is not None:
            raise ValueError("If initializer is a constant, do not specify shape.")
        initial_value = initializer
    else:
        # Instantiate initializer if provided initializer is a type object.
        if isinstance(initializer, type(init_ops.Initializer)):
            initializer = initializer(dtype=dtype)
        shape_list = None if shape is None else shape_object.as_list()
        if "partition_info" in tf_inspect.getargspec(initializer).args:
            initial_value = functools.partial(initializer,
                                              shape_list,
                                              dtype=dtype,
                                              partition_info=partition_info)
        else:
            initial_value = functools.partial(initializer,
                                              shape_list,
                                              dtype=dtype)

    exit(variables.VariableV1(
        initial_value=initial_value,
        name=name,
        dtype=variable_dtype,
        use_resource=True,
        **kwargs))
