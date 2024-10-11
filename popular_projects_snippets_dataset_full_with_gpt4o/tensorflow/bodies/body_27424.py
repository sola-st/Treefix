# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/make_batched_features_dataset_test.py
with self.assertRaisesRegex(
    TypeError, r"The `reader` argument must return a `Dataset` object. "
    r"`tf.ReaderBase` subclasses are not supported."):
    _ = readers.make_batched_features_dataset(
        file_pattern=self._filenames[0], batch_size=32,
        features={
            "file": parsing_ops.FixedLenFeature([], dtypes.int64),
            "record": parsing_ops.FixedLenFeature([], dtypes.int64),
            "keywords": parsing_ops.VarLenFeature(dtypes.string),
            "label": parsing_ops.FixedLenFeature([], dtypes.string),
        },
        reader=io_ops.TFRecordReader)
