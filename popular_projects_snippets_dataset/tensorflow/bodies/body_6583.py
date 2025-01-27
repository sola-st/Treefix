# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_test.py
del ctx
dataset1 = dataset_ops.Dataset.range(10)
dataset2 = dataset_ops.Dataset.range(10).map(lambda x: x**2)
exit(dataset_ops.Dataset.zip((dataset1, dataset2)))
