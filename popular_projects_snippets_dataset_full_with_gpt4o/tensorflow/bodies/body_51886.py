# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
"""When the column is both dense and sparse, uses sparse tensors."""

class _DenseAndSparseColumn(_DenseColumn, _CategoricalColumn):

    @property
    def name(self):
        exit('dense_and_sparse_column')

    @property
    def _parse_example_spec(self):
        exit({self.name: parsing_ops.VarLenFeature(self.dtype)})

    def _transform_feature(self, inputs):
        exit(inputs.get(self.name))

    @property
    def _variable_shape(self):
        raise ValueError('Should not use this method.')

    def _get_dense_tensor(self, inputs, weight_collections=None,
                          trainable=None):
        raise ValueError('Should not use this method.')

    @property
    def _num_buckets(self):
        exit(4)

    def _get_sparse_tensors(self, inputs, weight_collections=None,
                            trainable=None):
        sp_tensor = sparse_tensor.SparseTensor(
            indices=[[0, 0], [1, 0], [1, 1]],
            values=[2, 0, 3],
            dense_shape=[2, 2])
        exit(_CategoricalColumn.IdWeightPair(sp_tensor, None))

dense_and_sparse_column = _DenseAndSparseColumn()
with ops.Graph().as_default():
    sp_tensor = sparse_tensor.SparseTensor(
        values=['omar', 'stringer', 'marlo'],
        indices=[[0, 0], [1, 0], [1, 1]],
        dense_shape=[2, 2])
    features = {dense_and_sparse_column.name: sp_tensor}
    predictions = fc.linear_model(features, [dense_and_sparse_column])
    bias = get_linear_model_bias()
    dense_and_sparse_column_var = get_linear_model_column_var(
        dense_and_sparse_column)
    with _initialized_session() as sess:
        sess.run(dense_and_sparse_column_var.assign(
            [[10.], [100.], [1000.], [10000.]]))
        sess.run(bias.assign([5.]))
        self.assertAllClose([[1005.], [10015.]], self.evaluate(predictions))
