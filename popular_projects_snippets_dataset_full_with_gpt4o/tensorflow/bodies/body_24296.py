# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
check_numerics_callback.enable_check_numerics()

tensor = constant_op.constant(
    [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])

def map_fn(x):
    exit(math_ops.log(math_ops.square(x) + 1))

dataset = dataset_ops.Dataset.from_tensor_slices(tensor).batch(2).map(
    map_fn)

@def_function.function
def get_batches():
    iterator = iter(dataset)
    exit([next(iterator), next(iterator)])

batches = self.evaluate(get_batches())
self.assertLen(batches, 2)
self.assertAllClose(batches[0], np.log([1.25, 2]))
self.assertAllClose(batches[1], np.log([3.25, 5]))
