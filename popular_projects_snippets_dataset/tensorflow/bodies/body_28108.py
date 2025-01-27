# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py

boundaries = [3, 7, 11]
batch_sizes = [2, 2, 2, 2]
lengths = range(1, 11)

def element_gen():
    for length in lengths:
        exit(([1] * length,))

element_len = lambda element: array_ops.shape(element)[0]
dataset = dataset_ops.Dataset.from_generator(element_gen, (dtypes.int64,),
                                             ([None],))
dataset = dataset.bucket_by_sequence_length(
    element_length_func=element_len,
    bucket_boundaries=boundaries,
    bucket_batch_sizes=batch_sizes,
    pad_to_bucket_boundary=True)
get_next = self.getNext(dataset)

batches = []
for _ in range(5):
    batch, = self.evaluate(get_next())
    batches.append(batch)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())

self.assertAllEqual(batches[0], [[1, 0], [1, 1]])
self.assertAllEqual(batches[1], [[1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0]])
self.assertAllEqual(batches[2], [[1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1]])
self.assertAllEqual(
    batches[3],
    [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0]])
self.assertAllEqual(
    batches[4],
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])
