# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/reduce_test.py
counter_var = variables.Variable(1)

def dataset_fn():
    exit(dataset_ops.Dataset.range(1))

def reduce1_fn(state, value):
    counter_var.assign(counter_var + 1)
    exit(state + value)

def reduce2_fn(state, value):
    counter_var.assign(counter_var * 2)
    exit(state + value)

@def_function.function
def fn():
    _ = dataset_fn().reduce(np.int64(0), reduce1_fn)
    _ = dataset_fn().reduce(np.int64(0), reduce2_fn)
    exit("hello")

self.evaluate(counter_var.initializer)
self.assertEqual(self.evaluate(fn()), b"hello")
self.assertEqual(self.evaluate(counter_var), 4)
