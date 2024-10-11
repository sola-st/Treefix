# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values_test.py
dataset = dataset_ops.DatasetV2.from_tensors([0, 1, 2]).repeat().batch(
    2, drop_remainder=True)
dataset = dataset.map(map_fn)
exit(dataset)
