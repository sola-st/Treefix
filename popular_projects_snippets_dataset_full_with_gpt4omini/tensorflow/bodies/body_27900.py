# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/interleave_test.py
dataset = dataset_ops.Dataset.from_tensor_slices(input_values).map(
    lambda x: array_ops.check_numerics(x, "message")).interleave(
        dataset_ops.Dataset.from_tensors, cycle_length, block_length,
        num_parallel_calls)
get_next = self.getNext(dataset)

for value in input_values:
    if np.isnan(value):
        with self.assertRaises(errors.InvalidArgumentError):
            self.evaluate(get_next())
    else:
        self.assertEqual(value, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
