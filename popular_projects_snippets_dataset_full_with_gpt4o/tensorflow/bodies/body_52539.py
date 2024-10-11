# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
wire_cast = fc.categorical_column_with_hash_bucket('wire_cast', 4)
with ops.Graph().as_default() as g:
    wire_tensor = sparse_tensor.SparseTensor(
        values=['omar'], indices=[[0, 0]], dense_shape=[1, 1])
    features = {'wire_cast': wire_tensor}
    fc_old.linear_model(features, [wire_cast], trainable=False)
    trainable_vars = g.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    self.assertEqual([], trainable_vars)
