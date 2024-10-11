# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_tf_record_dataset_test.py
if file_index is None:
    file_pattern = self._filenames
else:
    file_pattern = self._filenames[file_index]

if parser_fn:
    fn = lambda x: string_ops.substr(x, 1, 999)
else:
    fn = None

outputs = self.getNext(
    readers.make_tf_record_dataset(
        file_pattern=file_pattern,
        num_epochs=num_epochs,
        batch_size=batch_size,
        parser_fn=fn,
        num_parallel_reads=num_parallel_reads,
        drop_final_batch=drop_final_batch,
        shuffle=False))
self._verify_records(
    outputs,
    batch_size,
    file_index,
    num_epochs=num_epochs,
    interleave_cycle_length=num_parallel_reads,
    drop_final_batch=drop_final_batch,
    use_parser_fn=parser_fn)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(outputs())
