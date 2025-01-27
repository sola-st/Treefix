# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
"""Test saving and loading ShardedVariable with different numbers of shards.

    Loading tf.Variables into multiple Shards is not yet supported

    Args:
      shard_config: The number of shards to use before and after loading. For
        example, [2, 1] means to create and save the variable with 2 shards and
        load it into 1 shard (i.e., a regular tf.Variable).
    """
strategy = self._create_strategy(shard_config[0])

with strategy.scope():
    var = variables_lib.Variable([1., 2., 3., 4., 5., 6.])

# Save variable
model_dir = self.get_temp_dir()
save.save(var, model_dir)

strategy2 = self._create_strategy(shard_config[1])
with strategy2.scope():
    # Load variable
    loaded = load.load(model_dir)

# Assert all values loaded, values are same
if shard_config[1] > 1:
    loaded = array_ops.concat(loaded.variables, axis=0)
self.assertLen(loaded.numpy(), 6)

if shard_config[0] > 1:
    var = array_ops.concat(var.variables, axis=0)
self.assertAllClose(var.numpy(), loaded.numpy())
