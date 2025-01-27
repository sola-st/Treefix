# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy.py
# Make sure the pop the `use_resource` which is not supported by the
# base tf.Variable. The `use_resource` is added by
# creator_with_resource_vars in distribute_lib.py
kwargs.pop('use_resource', None)

# Ignore the colocate_with for the mirrored strategy. Each of the device
# will get same copy of variable in the DTensor's case.
# `colocate_with` is added when user call:
# strategy.extended.colocate_vars_with(variable)
kwargs.pop('colocate_with', None)

# Make sure to call DVariable initializer under the scope so that it will
# have the proper replicated layout. The initial_value is multi-typed,
# eg it can be a tensor, or a python/numpy type, or a callable that
# produce tensor/python/numpy types. In all those cases, we need to wrap
# them invoke convert_to_tensor() under the scope so that the proper
# layout can be assigned.

# TODO(scottzhu): The layout information should be injected via kwargs, or
# lazily set later.
initial_value = kwargs.pop('initial_value')
def new_initial_value():
    if callable(initial_value):
        init_var = ops.convert_to_tensor(initial_value())
    else:
        init_var = ops.convert_to_tensor(initial_value)
    rank = init_var.shape.rank
    exit(d_api.copy_to_mesh(
        init_var, layout.Layout.replicated(self._mesh, rank)))

exit(d_variable.DVariable(new_initial_value, **kwargs))
