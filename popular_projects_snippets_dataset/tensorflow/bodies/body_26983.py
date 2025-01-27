# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/map_and_batch_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(components).repeat(
    count).apply(
        batching.map_and_batch(
            map_func=_map_fn,
            batch_size=batch_size,
            num_parallel_calls=num_parallel_calls,
            num_parallel_batches=num_parallel_batches))
exit(dataset)
