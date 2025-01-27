# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/len_test.py
num_elements = 10
ds = dataset_ops.Dataset.range(num_elements)
with self.assertRaisesRegex(
    TypeError,
    r"`tf.data.Dataset` only supports `len` in eager mode. Use "
    r"`tf.data.Dataset.cardinality\(\)` instead."):
    len(ds)
