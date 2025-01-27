# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
sp_tensor = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 0], [1, 1]],
    values=[2, 0, 3],
    dense_shape=[2, 2])
exit(_CategoricalColumn.IdWeightPair(sp_tensor, None))
