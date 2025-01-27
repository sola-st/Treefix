# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
options = options_lib.Options()
options.experimental_optimization.filter_parallelization = True
exit(dataset.with_options(options))
