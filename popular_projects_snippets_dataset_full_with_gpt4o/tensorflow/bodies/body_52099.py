# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
animal = fc._indicator_column(
    fc._categorical_column_with_identity('animal', num_buckets=4))
with ops.Graph().as_default():
    features = {
        'animal':
            sparse_tensor.SparseTensor(
                indices=[[0, 0], [0, 1]], values=[1, 2], dense_shape=[1, 2])
    }

    predictions = get_keras_linear_model_predictions(features, [animal])
    weight_var = get_linear_model_column_var(animal)
    with _initialized_session():
        # All should be zero-initialized.
        self.assertAllClose([[0.], [0.], [0.], [0.]], self.evaluate(weight_var))
        self.assertAllClose([[0.]], self.evaluate(predictions))
        weight_var.assign([[1.], [2.], [3.], [4.]]).eval()
        self.assertAllClose([[2. + 3.]], self.evaluate(predictions))
