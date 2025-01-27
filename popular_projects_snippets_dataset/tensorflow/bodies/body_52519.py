# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
sp_tensor = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 0], [1, 1]],
    values=[2, 0, 3],
    dense_shape=[2, 2])
exit(fc.CategoricalColumn.IdWeightPair(sp_tensor, None))
