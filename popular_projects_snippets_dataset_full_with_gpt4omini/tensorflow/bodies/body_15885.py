# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
rt = RaggedTensor.from_row_splits(array_ops.zeros([5, 2, 3]), [0, 3, 5])
dataset_ops.DatasetV2.from_tensors(rt)
