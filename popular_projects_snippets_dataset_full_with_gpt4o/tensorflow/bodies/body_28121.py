# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_test_base.py
self.filenames = filenames
self.num_epochs = num_epochs
self.batch_size = batch_size

exit(readers.make_batched_features_dataset(
    file_pattern=self.filenames,
    batch_size=self.batch_size,
    features={
        "file": parsing_ops.FixedLenFeature([], dtypes.int64),
        "record": parsing_ops.FixedLenFeature([], dtypes.int64),
        "keywords": parsing_ops.VarLenFeature(dtypes.string),
        "label": parsing_ops.FixedLenFeature([], dtypes.string),
    },
    label_key=label_key,
    reader=core_readers.TFRecordDataset,
    num_epochs=self.num_epochs,
    shuffle=shuffle,
    shuffle_seed=shuffle_seed,
    reader_num_threads=reader_num_threads,
    parser_num_threads=parser_num_threads,
    drop_final_batch=drop_final_batch))
