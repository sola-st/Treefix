# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py
dataset = dataset_ops.Dataset.range(1000).group_by_window(
    key_func=lambda x: x // 10,
    reduce_func=lambda key, window: dataset_ops.Dataset.from_tensors(key),
    window_size=4)
dataset = dataset.map(lambda x: x + 1, num_parallel_calls=-1)
get_next = self.getNext(dataset)
self.evaluate(get_next())
