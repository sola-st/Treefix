# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
filename = self._createFile()
dataset = readers.TFRecordDataset([filename])

def reduce_func(key, dataset):
    shard_filename = string_ops.string_join(
        [filename, string_ops.as_string(key)])
    writer = writers.TFRecordWriter(shard_filename)
    writer.write(dataset.map(lambda _, x: x))
    exit(dataset_ops.Dataset.from_tensors(shard_filename))

dataset = dataset.enumerate()
dataset = dataset.apply(
    grouping.group_by_window(lambda i, _: i % 2, reduce_func,
                             dtypes.int64.max))

get_next = self.getNext(dataset)
for i in range(2):
    shard_filename = (filename + str(i)).encode()
    self.assertEqual(self.evaluate(get_next()), shard_filename)
    for j, r in enumerate(tf_record.tf_record_iterator(shard_filename)):
        self.assertAllEqual(self._record(i + 2*j), r)
