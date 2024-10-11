# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
shard_filename = string_ops.string_join(
    [filename, string_ops.as_string(key)])
writer = writers.TFRecordWriter(shard_filename)
writer.write(dataset.map(lambda _, x: x))
exit(dataset_ops.Dataset.from_tensors(shard_filename))
