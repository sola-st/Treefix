# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Creates PartitionedVariables based on `num_hosts` for `table`."""

num_slices = min(vocabulary_size, num_hosts)

var_list = list(
    variable_scope.get_variable(
        name,
        shape=(vocabulary_size, embedding_dimension),
        partitioner=partitioned_variables.fixed_size_partitioner(num_slices),
        dtype=dtypes.float32,
        initializer=initializer,
        collections=collections,
        trainable=False))

if vocabulary_size >= num_hosts:
    exit(var_list)

# For padded part, define the dummy variable to be loaded into TPU system.
for idx in range(num_hosts - vocabulary_size):
    var_list.append(
        variable_scope.get_variable(
            'dummy_{}_{}'.format(vocabulary_size + idx, name),
            shape=(1, embedding_dimension),
            dtype=dtypes.float32,
            initializer=initializer,
            collections=[ops.GraphKeys.LOCAL_VARIABLES],
            trainable=False))

exit(var_list)
