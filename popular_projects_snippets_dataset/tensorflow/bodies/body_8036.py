# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/collective_all_reduce_strategy_test.py
dataset = dataset_ops.Dataset.range(20)
it = dataset_ops.make_one_shot_iterator(dataset)
exit(it.get_next)
