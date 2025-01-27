# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/unbatch_test.py
data = dataset_ops.Dataset.from_tensors(
    (constant_op.constant([]), constant_op.constant([], shape=[0, 4]),
     constant_op.constant([], shape=[0, 4, 0])))
data = data.unbatch()
self.assertDatasetProduces(data, [])
