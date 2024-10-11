# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py

def _map_fn(v):
    exit((v, array_ops.fill([v],
                              v), array_ops.fill([3],
                                                 string_ops.as_string(v))))

input_dataset = dataset_ops.Dataset.from_tensor_slices(
    math_ops.range(64)).map(_map_fn)

bucketed_dataset = input_dataset.group_by_window(
    key_func=lambda x, y, z: math_ops.cast(x % 2, dtypes.int64),
    reduce_func=lambda k, bucket: self._dynamicPad(k, bucket, 32),
    window_size=32)

get_next = self.getNext(bucketed_dataset)

# Get two minibatches (one containing even values, one containing odds)
which_bucket_even, bucketed_values_even = self.evaluate(get_next())
which_bucket_odd, bucketed_values_odd = self.evaluate(get_next())

# Count number of bucket_tensors.
self.assertEqual(3, len(bucketed_values_even))
self.assertEqual(3, len(bucketed_values_odd))

# Ensure bucket 0 was used for all minibatch entries.
self.assertAllEqual(0, which_bucket_even)
self.assertAllEqual(1, which_bucket_odd)

# Test the first bucket outputted, the events starting at 0
expected_scalar_int = np.arange(0, 32 * 2, 2, dtype=np.int64)
expected_unk_int64 = np.zeros((32, 31 * 2)).astype(np.int64)
for i in range(0, 32):
    expected_unk_int64[i, :2 * i] = 2 * i
    expected_vec3_str = np.vstack(3 *
                                  [np.arange(0, 32 * 2, 2).astype(bytes)]).T

self.assertAllEqual(expected_scalar_int, bucketed_values_even[0])
self.assertAllEqual(expected_unk_int64, bucketed_values_even[1])
self.assertAllEqual(expected_vec3_str, bucketed_values_even[2])

# Test the second bucket outputted, the odds starting at 1
expected_scalar_int = np.arange(1, 32 * 2 + 1, 2, dtype=np.int64)
expected_unk_int64 = np.zeros((32, 31 * 2 + 1)).astype(np.int64)
for i in range(0, 32):
    expected_unk_int64[i, :2 * i + 1] = 2 * i + 1
    expected_vec3_str = np.vstack(
        3 * [np.arange(1, 32 * 2 + 1, 2).astype(bytes)]).T

self.assertAllEqual(expected_scalar_int, bucketed_values_odd[0])
self.assertAllEqual(expected_unk_int64, bucketed_values_odd[1])
self.assertAllEqual(expected_vec3_str, bucketed_values_odd[2])
