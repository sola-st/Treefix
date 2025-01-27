# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/len_test.py
num_elements = 10
ds = dataset_ops.Dataset.range(num_elements).filter(lambda x: True)
with self.assertRaisesRegex(TypeError, "unknown"):
    len(ds)
