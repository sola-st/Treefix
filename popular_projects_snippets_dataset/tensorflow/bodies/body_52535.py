# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
wire_cast = fc.categorical_column_with_hash_bucket('wire_cast', 4)
with ops.Graph().as_default() as g:
    wire_tensor = sparse_tensor.SparseTensor(
        values=['omar'], indices=[[0, 0]], dense_shape=[1, 1])
    features = {'wire_cast': wire_tensor}
    fc_old.linear_model(features, [wire_cast], weight_collections=['my-vars'])
    my_vars = g.get_collection('my-vars')
    bias = get_linear_model_bias()
    wire_cast_var = get_linear_model_column_var(wire_cast)
    self.assertIn(bias, my_vars)
    self.assertIn(wire_cast_var, my_vars)
