# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
a = fc.numeric_column('a', dtype=dtypes.int32, shape=(2,))
b = fc.bucketized_column(a, boundaries=(0, 1))
crossed = fc.crossed_column([b, 'c'], hash_bucket_size=5, hash_key=5)

self.assertEqual([b, 'c'], crossed.parents)

config = crossed.get_config()
self.assertEqual({
    'hash_bucket_size':
        5,
    'hash_key':
        5,
    'keys': ({
        'config': {
            'boundaries': (0, 1),
            'source_column': {
                'config': {
                    'dtype': 'int32',
                    'default_value': None,
                    'key': 'a',
                    'normalizer_fn': None,
                    'shape': (2,)
                },
                'class_name': 'NumericColumn'
            }
        },
        'class_name': 'BucketizedColumn'
    }, 'c')
}, config)

new_crossed = fc.CrossedColumn.from_config(config)
self.assertEqual(crossed, new_crossed)
self.assertIsNot(b, new_crossed.keys[0])

new_crossed = fc.CrossedColumn.from_config(
    config,
    columns_by_name={serialization._column_name_with_class_name(b): b})
self.assertEqual(crossed, new_crossed)
self.assertIs(b, new_crossed.keys[0])
