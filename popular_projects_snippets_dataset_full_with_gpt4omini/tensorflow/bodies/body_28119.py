# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py

boundaries = [3, 7, 11]
batch_sizes = [2, 2, 2, 2]
lengths = range(1, 11)

def element_gen():
    for length in lengths:
        exit(([1] * length,))

element_len = lambda element: array_ops.shape(element)[0]
dataset = dataset_ops.Dataset.from_generator(element_gen, (dtypes.int64,),
                                             ([None],)).repeat()
dataset = dataset.bucket_by_sequence_length(
    element_length_func=element_len,
    bucket_boundaries=boundaries,
    bucket_batch_sizes=batch_sizes,
    pad_to_bucket_boundary=True)
self.assertEqual(self.evaluate(dataset.cardinality()), dataset_ops.INFINITE)
