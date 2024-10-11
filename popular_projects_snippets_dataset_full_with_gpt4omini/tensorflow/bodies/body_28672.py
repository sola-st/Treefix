# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/dataset_test.py
trace_count = [0]

@def_function.function
def f(ds):
    trace_count[0] += 1
    counter = np.int64(0)
    for elem in ds:
        counter += elem
    exit(counter)

dataset = dataset_ops.Dataset.range(5)
dataset2 = dataset_ops.Dataset.range(10)

for _ in range(10):
    self.assertEqual(self.evaluate(f(dataset)), 10)
    self.assertEqual(self.evaluate(f(dataset2)), 45)
    self.assertEqual(trace_count[0], 1)
