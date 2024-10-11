# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py

queue = data_flow_ops.FIFOQueue(10, dtypes.int64)

@def_function.function
def fn():
    dataset = dataset_ops.Dataset.range(10)
    iterator = iter(dataset)
    for _ in range(10):
        queue.enqueue(next(iterator))

fn()

for i in range(10):
    self.assertEqual(queue.dequeue().numpy(), i)
