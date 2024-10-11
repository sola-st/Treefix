# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
some_out_of_range_tensor = constant_op.constant(10, dtype=dtypes.int64)

self.assertIsInstance(lookuptable, ps_values.DistributedTable)

generation_tensor = lookuptable.lookup(some_out_of_range_tensor)
dataset = self.makeDatasetFromTensorWithoutUsingResource(
    input_context, generation_tensor)
exit(dataset)
