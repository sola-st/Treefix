# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price', shape=[2])
bucketized_price = fc.bucketized_column(price, boundaries=[0, 2, 4, 6])
with ops.Graph().as_default():
    transformed_tensor = fc._transform_features_v2({
        'price': [[-1., 1.], [5., 6.]]
    }, [bucketized_price], None)

    self.evaluate(variables_lib.global_variables_initializer())
    self.evaluate(lookup_ops.tables_initializer())

    self.assertAllEqual([[0, 1], [3, 4]],
                        self.evaluate(transformed_tensor[bucketized_price]))
