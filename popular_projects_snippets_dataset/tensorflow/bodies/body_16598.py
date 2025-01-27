# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops_test.py
with ops.Graph().as_default():
    # The transposition array should be a constant if the rank of "values" is
    # statically known.
    tensor = random_ops.random_uniform(
        # Rank is statically known to be 5, but the dimension lengths are not
        # known.
        random_ops.random_uniform(
            shape=(5,), minval=0, maxval=10, dtype=dtypes.int32))
    sort_ops.sort(tensor, axis=1)
    transposition = (
        ops.get_default_graph().get_tensor_by_name('sort/transposition:0'))
    self.assertIsNot(tensor_util.constant_value(transposition), None)
    self.assertAllEqual(
        # Swaps "1" and "4" to put "1" at the end.
        tensor_util.constant_value(transposition),
        [0, 4, 2, 3, 1])
