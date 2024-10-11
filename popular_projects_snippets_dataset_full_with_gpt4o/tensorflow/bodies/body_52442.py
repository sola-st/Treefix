# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
price = fc.numeric_column('price', shape=[2])
bucketized_price = fc.bucketized_column(price, boundaries=[0, 2, 4, 6])
self.assertEqual([price], bucketized_price.parents)

config = bucketized_price.get_config()
self.assertEqual({
    'source_column': {
        'class_name': 'NumericColumn',
        'config': {
            'key': 'price',
            'shape': (2,),
            'default_value': None,
            'dtype': 'float32',
            'normalizer_fn': None
        }
    },
    'boundaries': (0, 2, 4, 6)
}, config)

new_bucketized_price = fc.BucketizedColumn.from_config(config)
self.assertEqual(bucketized_price, new_bucketized_price)
self.assertIsNot(price, new_bucketized_price.source_column)

new_bucketized_price = fc.BucketizedColumn.from_config(
    config,
    columns_by_name={
        serialization._column_name_with_class_name(price): price
    })
self.assertEqual(bucketized_price, new_bucketized_price)
self.assertIs(price, new_bucketized_price.source_column)
