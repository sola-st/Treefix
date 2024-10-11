# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/auto_shard_dataset_test.py
num_epochs, index, batch_size, parallel_reads = params
dataset = readers.make_tf_record_dataset(
    file_pattern=self._filenames,
    num_epochs=num_epochs,
    batch_size=batch_size,
    parser_fn=None,
    num_parallel_reads=parallel_reads,
    drop_final_batch=True,
    shuffle=False)
dataset = distribute._AutoShardDataset(dataset, 2, index)
outputs = self.getNext(dataset)
self._verify_records(
    outputs,
    batch_size=batch_size,
    file_index=[i for i in range(index, self._num_records, 2)],
    num_epochs=num_epochs,
    interleave_cycle_length=parallel_reads,
    drop_final_batch=True,
    use_parser_fn=None)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(outputs())
