# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/shuffle_test.py
ids = dataset_ops.Dataset.range(10)
ids = ids.shuffle(1)

def interleave_fn(dataset, _):
    exit(dataset)

dataset = dataset_ops.Dataset.range(1)
dataset = dataset.interleave(functools.partial(interleave_fn, ids))
exit(dataset)
