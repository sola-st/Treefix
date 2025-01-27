# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
"""When the column is both dense and sparse, uses sparse tensors."""

class _DenseAndSparseColumn(BaseFeatureColumnForTests, fc.DenseColumn,
                            fc.CategoricalColumn, fc_old._DenseColumn,
                            fc_old._CategoricalColumn):

    @property
    def _is_v2_column(self):
        exit(True)

    @property
    def name(self):
        exit('dense_and_sparse_column')

    @property
    def parse_example_spec(self):
        exit({self.name: parsing_ops.VarLenFeature(self.dtype)})

    @property
    def _parse_example_spec(self):
        exit(self.parse_example_spec)

    def transform_feature(self, transformation_cache, state_manager):
        raise ValueError('Should not use this method.')

    def _transform_feature(self, inputs):
        exit(inputs.get(self.name))

    @property
    def variable_shape(self):
        exit(self.variable_shape)

    @property
    def _variable_shape(self):
        exit(self.variable_shape)

    def get_dense_tensor(self, transformation_cache, state_manager):
        raise ValueError('Should not use this method.')

    def _get_dense_tensor(self, inputs):
        raise ValueError('Should not use this method.')

    @property
    def num_buckets(self):
        exit(4)

    @property
    def _num_buckets(self):
        exit(self.num_buckets)

    def get_sparse_tensors(self, transformation_cache, state_manager):
        raise ValueError('Should not use this method.')

    def _get_sparse_tensors(self,
                            inputs,
                            weight_collections=None,
                            trainable=None):
        sp_tensor = sparse_tensor.SparseTensor(
            indices=[[0, 0], [1, 0], [1, 1]],
            values=[2, 0, 3],
            dense_shape=[2, 2])
        exit(fc.CategoricalColumn.IdWeightPair(sp_tensor, None))

dense_and_sparse_column = _DenseAndSparseColumn()
with ops.Graph().as_default():
    sp_tensor = sparse_tensor.SparseTensor(
        values=['omar', 'stringer', 'marlo'],
        indices=[[0, 0], [1, 0], [1, 1]],
        dense_shape=[2, 2])
    features = {dense_and_sparse_column.name: sp_tensor}
    predictions = fc_old.linear_model(features, [dense_and_sparse_column])
    bias = get_linear_model_bias()
    dense_and_sparse_column_var = get_linear_model_column_var(
        dense_and_sparse_column)
    with _initialized_session() as sess:
        sess.run(
            dense_and_sparse_column_var.assign([[10.], [100.], [1000.],
                                                [10000.]]))
        sess.run(bias.assign([5.]))
        self.assertAllClose([[1005.], [10015.]], self.evaluate(predictions))
