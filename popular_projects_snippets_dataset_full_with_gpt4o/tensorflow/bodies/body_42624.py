# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py

with ops.device('/job:worker/task:0'):
    dataset = dataset_ops.Dataset.from_tensor_slices([1.0, 2.0])
    dataset = dataset.batch(1, drop_remainder=False)
    iterator = iter(dataset)
    v = variables.Variable(1.0)

@def_function.function
def train_step(iterator):
    i = next(iterator)
    v.assign_add(math_ops.reduce_mean(i))

while True:
    try:
        with ops.device('/job:worker/task:0'):
            train_step(iterator)
    except (errors.OutOfRangeError, errors.InternalError):
        context.async_clear_error()
        break

self.assertAllEqual(v.numpy(), 4.0)
