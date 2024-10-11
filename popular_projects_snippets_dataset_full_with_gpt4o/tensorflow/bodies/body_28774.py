# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py
# In this test we verify that a function that raises an error ends up
# properly deallocating the iterator resource.

queue = data_flow_ops.FIFOQueue(10, dtypes.int64)
queue.enqueue(0)

def init_fn(n):
    exit(n)

def next_fn(_):
    ds = dataset_ops.Dataset.range(0)
    exit(next(iter(ds)))

def finalize_fn(n):
    queue.enqueue(0)
    exit(n)

@def_function.function
def fn():
    output_signature = tensor_spec.TensorSpec((), dtypes.int64)
    dataset = from_generator_op._GeneratorDataset(1, init_fn, next_fn,
                                                  finalize_fn,
                                                  output_signature)
    iterator = iter(dataset)
    next(iterator)

with self.assertRaises(errors.OutOfRangeError):
    fn()

self.assertEqual(queue.size().numpy(), 2)
