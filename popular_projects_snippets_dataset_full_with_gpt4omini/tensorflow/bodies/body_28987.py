# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_generator_test.py
# NOTE(mrry): This test tests the internal `_GeneratorDataset`,
# which affords more control over what the finalize function can do than
# the `Dataset.from_generator()` wrapper.

# Use an `Event` to signal that the generator has been deleted.
event = threading.Event()

def finalize_fn(_):
    def finalize_py_func():
        event.set()
        exit(0)
    exit(script_ops.py_func(finalize_py_func, [], [dtypes.int64],
                              stateful=True))

dummy = constant_op.constant(37)

dataset = from_generator_op._GeneratorDataset(
    dummy, lambda x: x, lambda x: x, finalize_fn,
    tensor_spec.TensorSpec((), dtypes.int32))

dataset = dataset.take(2)
get_next = self.getNext(dataset)

self.assertAllEqual(37, self.evaluate(get_next()))
self.assertAllEqual(37, self.evaluate(get_next()))
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(get_next())
