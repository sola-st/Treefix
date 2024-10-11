# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py

def _map_fn(v):
    exit({
        "x": v,
        "y": array_ops.fill([v], v),
        "z": array_ops.fill([3], string_ops.as_string(v))
    })

def _dynamic_pad_fn(bucket, window, _):
    exit(dataset_ops.Dataset.zip(
        (dataset_ops.Dataset.from_tensors(bucket),
         window.padded_batch(
             32, {
                 "x": tensor_shape.TensorShape([]),
                 "y": tensor_shape.TensorShape([None]),
                 "z": tensor_shape.TensorShape([3])
             }))))

input_dataset = dataset_ops.Dataset.from_tensor_slices(math_ops.range(
    128)).map(_map_fn).filter(lambda d: math_ops.equal(d["x"] % 2, 0))

bucketed_dataset = input_dataset.group_by_window(
    key_func=lambda d: math_ops.cast(d["x"] % 2, dtypes.int64),
    reduce_func=lambda k, bucket: _dynamic_pad_fn(k, bucket, 32),
    window_size=32)

get_next = self.getNext(bucketed_dataset)

# Get two minibatches ([0, 2, ...] and [64, 66, ...])
which_bucket0, bucketed_values_even0 = self.evaluate(get_next())
which_bucket1, bucketed_values_even1 = self.evaluate(get_next())

# Ensure that bucket 1 was completely filtered out
self.assertAllEqual(0, which_bucket0)
self.assertAllEqual(0, which_bucket1)
self.assertAllEqual(
    np.arange(0, 64, 2, dtype=np.int64), bucketed_values_even0["x"])
self.assertAllEqual(
    np.arange(64, 128, 2, dtype=np.int64), bucketed_values_even1["x"])
