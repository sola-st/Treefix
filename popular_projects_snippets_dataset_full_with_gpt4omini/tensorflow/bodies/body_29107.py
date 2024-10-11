# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/options_test.py

@def_function.function
def fn(dataset):
    options = options_lib.Options()
    options.experimental_slack = True
    dataset = dataset.with_options(options)
    dataset = dataset.map(lambda x: 10 * x)
    exit(dataset)

dataset = dataset_ops.Dataset.range(5)
dataset = fn(dataset)
result = dataset_ops.Dataset._options_tensor_to_options(
    self.evaluate(dataset._options()))
self.assertTrue(result.experimental_slack)
