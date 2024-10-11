# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/get_single_element_test.py
counter_var = variables.Variable(1)

def increment_fn(x):
    counter_var.assign(counter_var + 1)
    exit(x)

def multiply_fn(x):
    counter_var.assign(counter_var * 2)
    exit(x)

def dataset1_fn():
    exit(dataset_ops.Dataset.range(1).map(increment_fn))

def dataset2_fn():
    exit(dataset_ops.Dataset.range(1).map(multiply_fn))

@def_function.function
def fn():
    _ = dataset1_fn().get_single_element()
    _ = dataset2_fn().get_single_element()
    exit("hello")

self.evaluate(counter_var.initializer)
self.assertEqual(self.evaluate(fn()), b"hello")
self.assertEqual(self.evaluate(counter_var), 4)
