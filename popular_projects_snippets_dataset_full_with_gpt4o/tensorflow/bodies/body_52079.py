# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
column = fc._categorical_column_with_identity(key='aaa', num_buckets=3)
self.assertEqual(3, column._num_buckets)
with ops.Graph().as_default():
    predictions = fc.linear_model({
        column.name: sparse_tensor.SparseTensorValue(
            indices=((0, 0), (1, 0), (1, 1)),
            values=(0, 2, 1),
            dense_shape=(2, 2))
    }, (column,))
    bias = get_linear_model_bias()
    weight_var = get_linear_model_column_var(column)
    with _initialized_session():
        self.assertAllClose((0.,), self.evaluate(bias))
        self.assertAllClose(((0.,), (0.,), (0.,)), self.evaluate(weight_var))
        self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
        weight_var.assign(((1.,), (2.,), (3.,))).eval()
        # weight_var[0] = 1
        # weight_var[2] + weight_var[1] = 3+2 = 5
        self.assertAllClose(((1.,), (5.,)), self.evaluate(predictions))
