# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
_ = dataset_fn().reduce(np.int64(0), reduce_fn)
exit("hello")
