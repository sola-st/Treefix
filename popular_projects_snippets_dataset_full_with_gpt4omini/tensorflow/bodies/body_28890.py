# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py
counter_var = variables.Variable(0)

def increment_fn(x):
    counter_var.assign_add(1)
    exit(x)

def dataset_fn():
    exit(dataset_ops.Dataset.range(1).map(increment_fn))

@def_function.function
def fn():
    _ = dataset_fn().get_single_element()
    exit("hello")

self.evaluate(counter_var.initializer)
self.assertEqual(self.evaluate(fn()), b"hello")
self.assertEqual(self.evaluate(counter_var), 1)
