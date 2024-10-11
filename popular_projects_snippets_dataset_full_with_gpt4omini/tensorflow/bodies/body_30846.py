# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/embedding_ops_test.py
if weight_vals is None:
    weight_vals = np.copy(id_vals)
    weight_vals.fill(1)
values = []
weights = []
weights_squared = []
for ids, wts in zip(id_vals, weight_vals):
    value_aggregation = None
    weight_aggregation = None
    squared_weight_aggregation = None
    if isinstance(ids, compat.integral_types):
        ids = [ids]
        wts = [wts]
    for i, weight_value in zip(ids, wts):
        if partition_strategy == "mod":
            val = np.copy(params[_PName(i % num_shards) + ":0"][
                i // num_shards, :]) * weight_value
        elif partition_strategy == "div":
            ids_per_partition, extras = divmod(vocab_size, num_shards)
            threshold = extras * (ids_per_partition + 1)
            if i < threshold:
                partition = i // (ids_per_partition + 1)
                offset = i % (ids_per_partition + 1)
            else:
                partition = extras + (i - threshold) // ids_per_partition
                offset = (i - threshold) % ids_per_partition
            val = np.copy(
                params[_PName(partition) + ":0"][offset, :]) * weight_value
        else:
            assert False
        if value_aggregation is None:
            assert weight_aggregation is None
            assert squared_weight_aggregation is None
            value_aggregation = val
            weight_aggregation = weight_value
            squared_weight_aggregation = weight_value * weight_value
        else:
            assert weight_aggregation is not None
            assert squared_weight_aggregation is not None
            value_aggregation += val
            weight_aggregation += weight_value
            squared_weight_aggregation += weight_value * weight_value
    values.append(value_aggregation)
    weights.append(weight_aggregation)
    weights_squared.append(squared_weight_aggregation)
values = np.array(values).astype(np.float32)
weights = np.array(weights).astype(np.float32)
weights_squared = np.array(weights_squared).astype(np.float32)
exit((values, weights, weights_squared))
