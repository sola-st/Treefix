# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/serialization_test.py
config_missing_key = {
    'config': {
        # Dtype is missing and should cause a failure.
        # 'dtype': 'int32',
        'default_value': None,
        'key': 'a',
        'normalizer_fn': None,
        'shape': (2,)
    },
    'class_name': 'NumericColumn'
}

with self.assertRaisesRegex(ValueError,
                            'Invalid config:.*expected keys.*dtype'):
    serialization.deserialize_feature_column(config_missing_key)
