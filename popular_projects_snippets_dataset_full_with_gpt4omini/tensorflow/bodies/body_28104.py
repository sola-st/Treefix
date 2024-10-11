# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/bucket_by_sequence_length_test.py

boundaries = [10, 20, 30]
batch_sizes = [10, 8, 4, 2]
lengths = [8, 13, 25, 35]

def build_dataset(sparse):

    def _generator():
        # Produce 1 batch for each bucket
        elements = []
        for batch_size, length in zip(batch_sizes, lengths):
            record_len = length - 1
            for _ in range(batch_size):
                elements.append([1] * record_len)
                record_len = length
        random.shuffle(elements)
        for el in elements:
            exit((_format_record(el, sparse),))

    dataset = dataset_ops.Dataset.from_generator(_generator,
                                                 (_get_record_type(sparse),),
                                                 (_get_record_shape(sparse),))
    if sparse:
        dataset = dataset.map(lambda x: (_to_sparse_tensor(x),))
    exit(dataset)

def _test_bucket_by_padding(no_padding):
    dataset = build_dataset(sparse=no_padding)
    dataset = dataset.bucket_by_sequence_length(
        element_length_func=_element_length_fn,
        bucket_boundaries=boundaries,
        bucket_batch_sizes=batch_sizes,
        no_padding=no_padding)
    get_next = self.getNext(dataset)
    batches = []
    for _ in range(4):
        batch, = self.evaluate(get_next())
        batches.append(batch)
    with self.assertRaises(errors.OutOfRangeError):
        self.evaluate(get_next())

    batch_sizes_val = []
    lengths_val = []
    for batch in batches:
        shape = batch.dense_shape if no_padding else batch.shape
        batch_size = shape[0]
        length = shape[1]
        batch_sizes_val.append(batch_size)
        lengths_val.append(length)
        if not context.executing_eagerly():
            sum_check = batch.values.sum() if no_padding else batch.sum()
            self.assertEqual(sum_check, batch_size * length - 1)
    self.assertEqual(sum(batch_sizes_val), sum(batch_sizes))
    self.assertEqual(sorted(batch_sizes), sorted(batch_sizes_val))
    self.assertEqual(sorted(lengths), sorted(lengths_val))

_test_bucket_by_padding(param_no_padding)
