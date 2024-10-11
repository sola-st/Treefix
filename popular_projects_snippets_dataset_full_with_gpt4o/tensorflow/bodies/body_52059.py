# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
wire_column = fc._categorical_column_with_vocabulary_list(
    key='aaa',
    vocabulary_list=('omar', 'stringer', 'marlo'),
    num_oov_buckets=1)
self.assertEqual(4, wire_column._num_buckets)
with ops.Graph().as_default():
    predictions = get_keras_linear_model_predictions({
        wire_column.name:
            sparse_tensor.SparseTensorValue(
                indices=((0, 0), (1, 0), (1, 1)),
                values=('marlo', 'skywalker', 'omar'),
                dense_shape=(2, 2))
    }, (wire_column,))
    bias = get_linear_model_bias()
    wire_var = get_linear_model_column_var(wire_column)
    with _initialized_session():
        self.assertAllClose((0.,), self.evaluate(bias))
        self.assertAllClose(((0.,), (0.,), (0.,), (0.,)),
                            self.evaluate(wire_var))
        self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
        wire_var.assign(((1.,), (2.,), (3.,), (4.,))).eval()
        # 'marlo' -> 2: wire_var[2] = 3
        # 'skywalker' -> 3, 'omar' -> 0: wire_var[3] + wire_var[0] = 4+1 = 5
        self.assertAllClose(((3.,), (5.,)), self.evaluate(predictions))
