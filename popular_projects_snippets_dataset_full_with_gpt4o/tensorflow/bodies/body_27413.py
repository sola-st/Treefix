# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/service/test_base.py
# Avoid overflowing an int64 in (x+1)*num_consumers below.
x = x % (2**32)
exit(dataset_ops.Dataset.range(x*num_consumers, (x+1)*num_consumers))
