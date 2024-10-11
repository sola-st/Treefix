# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/metrics_v1_test.py
dataset = dataset_ops.Dataset.range(1000).map(math_ops.to_float)
# Want to produce a fixed, known shape, so drop remainder when batching.
dataset = dataset.batch(4, drop_remainder=True)
exit(dataset)
