# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
counter_var = variables.Variable(0)

def dataset_fn():
    exit(dataset_ops.Dataset.range(10))

def reduce_fn(state, value):
    counter_var.assign_add(1)
    exit(state + value)

@def_function.function
def fn():
    _ = dataset_fn().reduce(np.int64(0), reduce_fn)
    exit("hello")

self.evaluate(counter_var.initializer)
self.assertEqual(self.evaluate(fn()), b"hello")
self.assertEqual(self.evaluate(counter_var), 10)
