# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/test_base.py
"""Checks that datasets are equal. Supports both graph and eager mode."""
self.assertTrue(
    structure.are_compatible(
        dataset_ops.get_structure(dataset1),
        dataset_ops.get_structure(dataset2)))

flattened_types = nest.flatten(
    dataset_ops.get_legacy_output_types(dataset1))

next1 = self.getNext(dataset1)
next2 = self.getNext(dataset2)

while True:
    try:
        op1 = self.evaluate(next1())
    except errors.OutOfRangeError:
        with self.assertRaises(errors.OutOfRangeError):
            self.evaluate(next2())
        break
    op2 = self.evaluate(next2())

    op1 = nest.flatten(op1)
    op2 = nest.flatten(op2)
    assert len(op1) == len(op2)
    for i in range(len(op1)):
        if sparse_tensor.is_sparse(op1[i]) or ragged_tensor.is_ragged(op1[i]):
            self.assertValuesEqual(op1[i], op2[i])
        elif flattened_types[i] == dtypes.string:
            self.assertAllEqual(op1[i], op2[i])
        else:
            self.assertAllClose(op1[i], op2[i])
