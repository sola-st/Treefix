# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
wire_cast = fc._categorical_column_with_hash_bucket('wire_cast', 4)
with ops.Graph().as_default() as g:
    wire_tensor = sparse_tensor.SparseTensor(
        values=['omar'], indices=[[0, 0]], dense_shape=[1, 1])
    features = {'wire_cast': wire_tensor}
    get_keras_linear_model_predictions(features, [wire_cast], trainable=False)
    trainable_vars = g.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES)
    self.assertEqual([], trainable_vars)
