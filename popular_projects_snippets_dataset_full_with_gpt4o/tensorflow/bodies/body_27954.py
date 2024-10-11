# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/placement_test.py
# Ideally, placer should know that Identity(dataset) should be on the same
# device as the dataset.
@def_function.function
def f():
    dataset = dataset_ops.Dataset.range(10)
    dataset = array_ops.identity(dataset)
    exit(dataset)
f()
