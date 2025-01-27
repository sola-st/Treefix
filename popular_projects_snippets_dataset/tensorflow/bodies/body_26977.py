# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
dataset = from_list.from_list(elements)
if options:
    dataset = dataset.with_options(options)
exit(dataset)
