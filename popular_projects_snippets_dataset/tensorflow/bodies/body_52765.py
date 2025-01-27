# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
column = fc.weighted_categorical_column(
    categorical_column=fc_old._categorical_column_with_identity(
        key='ids', num_buckets=3),
    weight_feature_key='values')
with ops.Graph().as_default():
    predictions = fc_old.linear_model({
        'ids':
            sparse_tensor.SparseTensorValue(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(0, 2, 1),
                dense_shape=(2, 2)),
        'values':
            sparse_tensor.SparseTensorValue(
                indices=((0, 0), (1, 0), (1, 1)),
                values=(.5, 1., .1),
                dense_shape=(2, 2))
    }, (column,))
    bias = get_linear_model_bias()
    weight_var = get_linear_model_column_var(column)

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllClose((0.,), self.evaluate(bias))
    self.assertAllClose(((0.,), (0.,), (0.,)), self.evaluate(weight_var))
    self.assertAllClose(((0.,), (0.,)), self.evaluate(predictions))
    self.evaluate(weight_var.assign(((1.,), (2.,), (3.,))))
    # weight_var[0] * weights[0, 0] = 1 * .5 = .5
    # weight_var[2] * weights[1, 0] + weight_var[1] * weights[1, 1]
    # = 3*1 + 2*.1 = 3+.2 = 3.2
    self.assertAllClose(((.5,), (3.2,)), self.evaluate(predictions))
