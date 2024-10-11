# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
generation_tensor = constant_op.constant([0, 1, 3], dtype=dtypes.int64)
dataset = self.makeDatasetFromTensorWithoutUsingResource(
    input_context, generation_tensor)
dataset = dataset.map(map_fn)
exit(dataset)
