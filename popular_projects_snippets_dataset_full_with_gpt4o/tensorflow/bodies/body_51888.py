# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
wire_cast = fc._categorical_column_with_hash_bucket('wire_cast', 4)
with ops.Graph().as_default():
    wire_tensor = sparse_tensor.SparseTensor(
        values=['omar', 'stringer', 'marlo'],  # hashed to = [2, 0, 3]
        indices=[[0, 0], [1, 0], [1, 1]],
        dense_shape=[2, 2])
    features = {'wire_cast': wire_tensor}
    predictions = fc.linear_model(features, [wire_cast], units=3)
    bias = get_linear_model_bias()
    wire_cast_var = get_linear_model_column_var(wire_cast)
    with _initialized_session() as sess:
        self.assertAllClose(np.zeros((3,)), self.evaluate(bias))
        self.assertAllClose(np.zeros((4, 3)), self.evaluate(wire_cast_var))
        sess.run(
            wire_cast_var.assign([[10., 11., 12.], [100., 110., 120.], [
                1000., 1100., 1200.
            ], [10000., 11000., 12000.]]))
        sess.run(bias.assign([5., 6., 7.]))
        self.assertAllClose([[1005., 1106., 1207.], [10015., 11017., 12019.]],
                            self.evaluate(predictions))
