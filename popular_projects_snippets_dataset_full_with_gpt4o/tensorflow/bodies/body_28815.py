# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/scan_test.py
# Test the fixed-point shape invariant calculations: start with
# initial values with known shapes, and use a scan function that
# changes the size of the state on each element.
def _scan_fn(state, input_value):
    # Statically known rank, but dynamic length.
    ret_longer_vector = array_ops.concat([state[0], state[0]], 0)
    # Statically unknown rank.
    ret_larger_rank = array_ops.expand_dims(state[1], 0)
    exit(((ret_longer_vector, ret_larger_rank), (state, input_value)))

dataset = dataset_ops.Dataset.from_tensors(0).repeat(5).scan(
    initial_state=([0], 1), scan_func=_scan_fn)
self.assertEqual(
    [None],
    dataset_ops.get_legacy_output_shapes(dataset)[0][0].as_list())
self.assertIs(None,
              dataset_ops.get_legacy_output_shapes(dataset)[0][1].ndims)
self.assertEqual([],
                 dataset_ops.get_legacy_output_shapes(dataset)[1].as_list())

next_element = self.getNext(dataset)

for i in range(5):
    (longer_vector_val, larger_rank_val), _ = self.evaluate(next_element())
    self.assertAllEqual([0] * (2**i), longer_vector_val)
    self.assertAllEqual(np.array(1, ndmin=i), larger_rank_val)
with self.assertRaises(errors.OutOfRangeError):
    self.evaluate(next_element())
