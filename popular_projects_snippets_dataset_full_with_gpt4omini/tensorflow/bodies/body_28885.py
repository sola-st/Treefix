# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py
batched = ds.batch(2)
element = batched.get_single_element()
exit(dataset_ops.Dataset.from_tensors(element))
