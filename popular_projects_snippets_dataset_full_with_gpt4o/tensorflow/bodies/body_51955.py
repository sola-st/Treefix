# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
price1 = fc._numeric_column('price1')
price2 = fc._numeric_column('price2')
with ops.Graph().as_default():
    features = {
        'price1': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
        'price2': array_ops.placeholder(dtype=dtypes.int64),  # batchsize = 2
    }
    predictions = get_keras_linear_model_predictions(features,
                                                     [price1, price2])
    with _initialized_session() as sess:
        sess.run(
            predictions,
            feed_dict={
                features['price1']: [[1.], [5.]],
                features['price2']: [[1.], [5.]],
            })
