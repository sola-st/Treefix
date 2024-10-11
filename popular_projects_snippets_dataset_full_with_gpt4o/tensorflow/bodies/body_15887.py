# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape_test.py
ragged = DynamicRaggedShape.from_lengths([4, (3, 0, 4, 5)])
dataset_ops.DatasetV2.from_tensors(ragged)
