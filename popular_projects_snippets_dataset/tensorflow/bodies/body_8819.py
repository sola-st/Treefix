# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
data = random_ops.random_uniform((10, 10))
dataset = dataset_ops.DatasetV2.from_tensors([data]).repeat()
exit(dataset)
