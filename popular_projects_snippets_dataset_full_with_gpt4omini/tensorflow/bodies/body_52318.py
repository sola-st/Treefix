# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
inputs = sparse_tensor.SparseTensorValue(**inputs_args)
expected = sparse_tensor.SparseTensorValue(**expected_args)
column = sfc.sequence_categorical_column_with_vocabulary_file(
    key='aaa',
    vocabulary_file=self._wire_vocabulary_file_name,
    vocabulary_size=self._wire_vocabulary_size)

id_weight_pair = _get_sparse_tensors(column, {'aaa': inputs})

self.assertIsNone(id_weight_pair.weight_tensor)
self.evaluate(variables_lib.global_variables_initializer())
self.evaluate(lookup_ops.tables_initializer())
_assert_sparse_tensor_value(
    self, expected, self.evaluate(id_weight_pair.id_tensor))
