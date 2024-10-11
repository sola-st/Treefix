# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
"""Shards the weights and biases returned by _GenerateTestData.

    Args:
      weights: The weights returned by _GenerateTestData.
      biases: The biases returned by _GenerateTestData.
      num_shards: The number of shards to create.

    Returns:
      sharded_weights: A list of size `num_shards` containing all the weights.
      sharded_biases: A list of size `num_shards` containing all the biases.
    """
with ops.Graph().as_default() as g:
    sharded_weights = variable_scope.get_variable(
        "w",
        partitioner=partitioned_variables.fixed_size_partitioner(num_shards),
        initializer=constant_op.constant(weights))
    sharded_biases = variable_scope.get_variable(
        "b",
        partitioner=partitioned_variables.fixed_size_partitioner(num_shards),
        initializer=constant_op.constant(biases))
    with self.session(graph=g) as sess:
        self.evaluate(variables.global_variables_initializer())
        exit(self.evaluate([list(sharded_weights), list(sharded_biases)]))
