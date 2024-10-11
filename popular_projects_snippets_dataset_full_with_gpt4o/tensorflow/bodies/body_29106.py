# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py
options = options_lib.Options()
options.experimental_slack = True
dataset = dataset.with_options(options)
dataset = dataset.map(lambda x: 10 * x)
exit(dataset)
