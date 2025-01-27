# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
wire_cast = fc.categorical_column_with_hash_bucket('wire_cast', 4)
with ops.Graph().as_default():
    wire_tensor = array_ops.sparse_placeholder(dtypes.string)
    wire_value = sparse_tensor.SparseTensorValue(
        values=['omar', 'stringer', 'marlo', 'omar'],  # hashed = [2, 0, 3, 2]
        indices=[[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 0, 1]],
        dense_shape=[2, 2, 2])
    features = {'wire_cast': wire_tensor}
    predictions = fc_old.linear_model(features, [wire_cast])
    wire_cast_var = get_linear_model_column_var(wire_cast)
    with _initialized_session() as sess:
        self.assertAllClose(np.zeros((4, 1)), self.evaluate(wire_cast_var))
        self.assertAllClose(
            np.zeros((2, 1)),
            predictions.eval(feed_dict={wire_tensor: wire_value}))
        sess.run(wire_cast_var.assign([[10.], [100.], [1000.], [10000.]]))
        self.assertAllClose(
            [[1010.], [11000.]],
            predictions.eval(feed_dict={wire_tensor: wire_value}))
