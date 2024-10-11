# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/tf_record_dataset_test.py
with self.assertRaisesRegex(
    TypeError,
    "The `filenames` argument must contain `tf.string` elements. Got "
    "`tf.int32` elements."):
    readers.TFRecordDataset([1, 2, 3])
with self.assertRaisesRegex(
    TypeError,
    "The `filenames` argument must contain `tf.string` elements. Got "
    "`tf.int32` elements."):
    readers.TFRecordDataset(constant_op.constant([1, 2, 3]))
# convert_to_tensor raises different errors in graph and eager
with self.assertRaises(Exception):
    readers.TFRecordDataset(object())
