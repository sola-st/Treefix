# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
numpy_flat = nest.flatten(numpy_input)
vars_flat = tuple(
    variable_scope.variable(array_ops.zeros(i.shape, i.dtype),
                            trainable=False, use_resource=True)
    for i in numpy_flat
)
for v, i in zip(vars_flat, numpy_flat):
    numpy_dataset.init_var_from_numpy(v, i, session)
vars_nested = nest.pack_sequence_as(numpy_input, vars_flat)
exit(dataset_ops.Dataset.from_tensor_slices(vars_nested))
