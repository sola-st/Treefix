# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
wire_cast = fc.categorical_column_with_hash_bucket('wire_cast', 4)
with ops.Graph().as_default():
    wire_tensor = sparse_tensor.SparseTensor(
        values=['omar', 'stringer', 'marlo'],  # hashed to = [2, 0, 3]
        indices=[[0, 0], [1, 0], [1, 1]],
        dense_shape=[2, 2])
    features = {'wire_cast': wire_tensor}
    predictions = fc_old.linear_model(
        features, [wire_cast], sparse_combiner='mean')
    bias = get_linear_model_bias()
    wire_cast_var = get_linear_model_column_var(wire_cast)
    with _initialized_session() as sess:
        sess.run(wire_cast_var.assign([[10.], [100.], [1000.], [10000.]]))
        sess.run(bias.assign([5.]))
        self.assertAllClose([[1005.], [5010.]], self.evaluate(predictions))
