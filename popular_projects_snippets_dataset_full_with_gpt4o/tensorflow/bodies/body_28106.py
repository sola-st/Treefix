# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py

boundaries = [10, 20, 30]
batch_sizes = [10, 8, 4, 2]
lengths = [8, 13, 25]

def element_gen():
    # Produce 1 batch for each bucket
    elements = []
    for batch_size, length in zip(batch_sizes[:-1], lengths):
        for _ in range(batch_size):
            elements.append([1] * length)
    random.shuffle(elements)
    for el in elements:
        exit((el,))
    for _ in range(batch_sizes[-1]):
        el = [1] * (boundaries[-1] + 5)
        exit((el,))

element_len = lambda el: array_ops.shape(el)[0]
dataset = dataset_ops.Dataset.from_generator(element_gen, (dtypes.int64,),
                                             ([None],))
dataset = dataset.bucket_by_sequence_length(
    element_length_func=element_len,
    bucket_boundaries=boundaries,
    bucket_batch_sizes=batch_sizes,
    pad_to_bucket_boundary=True)
get_next = self.getNext(dataset)

batches = []
for _ in range(3):
    batch, = self.evaluate(get_next())
    batches.append(batch)
with self.assertRaisesOpError("bucket_boundaries"):
    self.evaluate(get_next())

batch_sizes_val = []
lengths_val = []
for batch in batches:
    batch_size = batch.shape[0]
    length = batch.shape[1]
    batch_sizes_val.append(batch_size)
    lengths_val.append(length)
batch_sizes = batch_sizes[:-1]
self.assertEqual(sum(batch_sizes_val), sum(batch_sizes))
self.assertEqual(sorted(batch_sizes), sorted(batch_sizes_val))
self.assertEqual([boundary - 1 for boundary in sorted(boundaries)],
                 sorted(lengths_val))
