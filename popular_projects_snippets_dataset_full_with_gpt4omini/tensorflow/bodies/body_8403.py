# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
if isinstance(element_spec, values.PerReplicaSpec):
    element_spec = element_spec._component_specs  # pylint: disable=protected-access
specs = nest.flatten_with_joined_string_paths(element_spec)
for path, spec in specs:
    if isinstance(spec, (sparse_tensor.SparseTensorSpec,
                         ragged_tensor.RaggedTensorSpec)):
        raise ValueError(
            "Found tensor {} with spec {}. TPUStrategy does not support "
            "distributed datasets with device prefetch when using sparse or "
            "ragged tensors. If you intend to use sparse or ragged tensors, "
            "please pass a tf.distribute.InputOptions object with "
            "experimental_fetch_to_device set to False to your dataset "
            "distribution function.".format(path, type(spec)))
