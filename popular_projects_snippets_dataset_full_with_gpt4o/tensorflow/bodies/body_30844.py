# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
p = []
params = {}
feed_dict = {}
if not shape:
    shape = [10]
for i in range(num_shards):
    shard_shape = [vocab_size // num_shards] + shape
    if i < vocab_size % num_shards:  # Excess goes evenly on the first shards
        shard_shape[0] += 1

    param_name = _PName(i)

    if use_shapeless_placeholder:
        param = array_ops.placeholder(dtype, shape=None, name=param_name)
    else:
        param = constant_op.constant(
            1.0, shape=shard_shape, dtype=dtype, name=param_name)
    p.append(param)
    np_type = "f" if dtype == dtypes.float32 else "d"
    val = (np.random.rand(*shard_shape).astype(np_type)) + 1
    params[param_name + ":0"] = val
    feed_dict[param.name] = val
exit((p, params, feed_dict))
