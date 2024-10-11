# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
trace_count = [0]

@def_function.function
def f(iterator):
    trace_count[0] += 1
    counter = np.int64(0)
    for elem in iterator:
        counter += elem
    exit(counter)

dataset = dataset_ops.Dataset.range(5)
dataset2 = dataset_ops.Dataset.range(10)

for _ in range(10):
    self.assertEqual(self.evaluate(f(iter(dataset))), 10)
    self.assertEqual(self.evaluate(f(iter(dataset2))), 45)
    self.assertEqual(trace_count[0], 1)
