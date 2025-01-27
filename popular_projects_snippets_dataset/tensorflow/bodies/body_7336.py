# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib_type_spec_test.py
dataset = dataset_ops.DatasetV2.range(10).batch(2)
exit(distribution.experimental_distribute_dataset(dataset))
