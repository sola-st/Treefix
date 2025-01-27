# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
assert isinstance(test_class, test_util.TensorFlowTestCase)
assert isinstance(actual, RowPartition)
assert isinstance(expected, RowPartition)

test_class.assertEqual(actual._has_precomputed_row_splits(),
                       expected._has_precomputed_row_splits())
test_class.assertEqual(actual._has_precomputed_row_lengths(),
                       expected._has_precomputed_row_lengths())
test_class.assertEqual(actual._has_precomputed_value_rowids(),
                       expected._has_precomputed_value_rowids())
test_class.assertEqual(actual._has_precomputed_nrows(),
                       expected._has_precomputed_nrows())
test_class.assertEqual(actual.uniform_row_length() is None,
                       expected.uniform_row_length() is None)

if expected._has_precomputed_row_splits():
    test_class.assertAllEqual(actual.row_splits(), expected.row_splits())
if expected._has_precomputed_row_lengths():
    test_class.assertAllEqual(actual.row_lengths(), expected.row_lengths())
if expected._has_precomputed_value_rowids():
    test_class.assertAllEqual(actual.value_rowids(), expected.value_rowids())
if expected._has_precomputed_nrows():
    test_class.assertAllEqual(actual.nrows(), expected.nrows())
if expected.uniform_row_length() is not None:
    test_class.assertAllEqual(actual.uniform_row_length(),
                              expected.uniform_row_length())
