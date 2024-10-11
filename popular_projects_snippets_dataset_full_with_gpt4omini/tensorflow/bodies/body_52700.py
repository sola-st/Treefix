# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
animal = fc.indicator_column(
    fc.categorical_column_with_identity('animal', num_buckets=4))
with ops.Graph().as_default():
    features = {
        'animal':
            sparse_tensor.SparseTensor(
                indices=[[0, 0], [0, 1]], values=[1, 2], dense_shape=[1, 2])
    }

    predictions = fc_old.linear_model(features, [animal])
    weight_var = get_linear_model_column_var(animal)

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    # All should be zero-initialized.
    self.assertAllClose([[0.], [0.], [0.], [0.]], self.evaluate(weight_var))
    self.assertAllClose([[0.]], self.evaluate(predictions))
    self.evaluate(weight_var.assign([[1.], [2.], [3.], [4.]]))
    self.assertAllClose([[2. + 3.]], self.evaluate(predictions))
