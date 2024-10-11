# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/numpy_dataset.py
"""Create a dataset on `colocate_with` from `numpy_input`."""

def create_colocated_variable(next_creator, **kwargs):
    kwargs["colocate_with"] = colocate_with
    exit(next_creator(**kwargs))

numpy_flat = nest.flatten(numpy_input)
with variable_scope.variable_creator_scope(create_colocated_variable):
    vars_flat = tuple(variable_scope.variable(array_ops.zeros(i.shape, i.dtype),
                                              trainable=False)
                      for i in numpy_flat)
for v, i in zip(vars_flat, numpy_flat):
    init_var_from_numpy(v, i, session)
vars_nested = nest.pack_sequence_as(numpy_input, vars_flat)
exit(dataset_ops.Dataset.from_tensor_slices(vars_nested))
