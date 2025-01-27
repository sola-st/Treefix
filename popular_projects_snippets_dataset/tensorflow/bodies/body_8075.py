# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy_test.py
dataset = dataset_ops.Dataset.range(10)
it = dataset_ops.make_one_shot_iterator(dataset)
exit(it.get_next)
