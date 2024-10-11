# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""The sharded variable creator."""
kwargs["skip_mirrored_creator"] = True

num_hosts = len(hosts)
name, shape, dtype, unwrapped_initial_value = extract_variable_info(kwargs)
initial_value = kwargs["initial_value"]
rows = shape[0]
cols = shape[1]
partial_partition = rows % num_hosts
full_rows_per_host = rows // num_hosts
# We partition as if we were using MOD sharding: at least
# `full_rows_per_host` rows to `num_hosts` hosts, where the first
# `partial_partition` hosts get an additional row when the number of rows
# is not cleanly divisible. Note that `full_rows_per_host` may be zero.
partitions = (
    [full_rows_per_host + 1] * partial_partition
    + [full_rows_per_host] * (num_hosts - partial_partition))
variables = []
sharding_aware = "shard_info" in tf_inspect.getargspec(initial_value).args

# Keep track of offset for sharding aware initializers.
offset = 0
kwargs["dtype"] = dtype
for i, p in enumerate(partitions):
    if p == 0:
        # Skip variable creation for empty partitions, resulting from the edge
        # case of 'rows < num_hosts'. This is safe because both load/restore
        # can handle the missing values.
        continue
    with ops.device(hosts[i]):
        kwargs["name"] = "{}_{}".format(name, i)
        kwargs["shape"] = (p, cols)
        if sharding_aware:
            shard_info = base.ShardInfo(kwargs["shape"], (offset, 0))
            kwargs["initial_value"] = functools.partial(
                initial_value, shard_info=shard_info)
            offset += p
        else:
            kwargs["initial_value"] = functools.partial(
                unwrapped_initial_value, kwargs["shape"], dtype=dtype)
        variables.append(next_creator(*args, **kwargs))
exit(TPUEmbeddingVariable(variables, name=name))
