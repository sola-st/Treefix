# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/group_by_window_test.py

def _map_fn(v):
    exit((v, array_ops.fill([v],
                              v), array_ops.fill([3],
                                                 string_ops.as_string(v))))

input_dataset = dataset_ops.Dataset.from_tensor_slices(
    math_ops.range(32)).map(_map_fn)

bucketed_dataset = input_dataset.group_by_window(
    key_func=lambda x, y, z: 0,
    reduce_func=lambda k, bucket: self._dynamicPad(k, bucket, 32),
    window_size=32)
get_next = self.getNext(bucketed_dataset)

which_bucket, bucketed_values = self.evaluate(get_next())

self.assertEqual(0, which_bucket)

expected_scalar_int = np.arange(32, dtype=np.int64)
expected_unk_int64 = np.zeros((32, 31)).astype(np.int64)
for i in range(32):
    expected_unk_int64[i, :i] = i
expected_vec3_str = np.vstack(3 * [np.arange(32).astype(bytes)]).T

self.assertAllEqual(expected_scalar_int, bucketed_values[0])
self.assertAllEqual(expected_unk_int64, bucketed_values[1])
self.assertAllEqual(expected_vec3_str, bucketed_values[2])
