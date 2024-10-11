# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
dataset = dataset_ops.Dataset.range(100)
it = dataset_ops.make_one_shot_iterator(dataset)
exit(it.get_next)
