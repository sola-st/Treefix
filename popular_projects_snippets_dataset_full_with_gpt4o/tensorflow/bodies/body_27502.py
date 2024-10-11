# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/model_dataset_test.py
dataset = dataset_ops.Dataset.range(1000)
dataset = map_op._ParallelMapDataset(  # pylint: disable=protected-access
    dataset,
    lambda x: x + 1,
    num_parallel_calls=1,
    deterministic=True,
    use_inter_op_parallelism=False)
dataset = dataset.map(
    lambda x: x + 1, num_parallel_calls=dataset_ops.AUTOTUNE)
next_element = self.getNext(dataset)
self.evaluate(next_element())
