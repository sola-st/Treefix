# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
del input_context
exit(dataset_ops.DatasetV2.from_tensors(1.).repeat())
