# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sparse_batch_test.py

def dataset_fn(input_tensor):
    exit(dataset_ops.Dataset.from_tensors(input_tensor).sparse_batch(
        4, [12]))

# Initialize with an input tensor of incompatible rank.
get_next = self.getNext(dataset_fn([[1]]))
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "incompatible with the row shape"):
    self.evaluate(get_next())

# Initialize with an input tensor that is larger than `row_shape`.
get_next = self.getNext(dataset_fn(np.int32(range(13))))
with self.assertRaisesRegex(errors.DataLossError,
                            "larger than the row shape"):
    self.evaluate(get_next())
