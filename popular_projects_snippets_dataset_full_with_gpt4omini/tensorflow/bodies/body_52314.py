# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/sequence_feature_column_test.py
"""Tests that column can be serialized."""
parent = sfc.sequence_categorical_column_with_identity(
    'animal', num_buckets=4)
animal = fc.indicator_column(parent)

config = animal.get_config()
self.assertEqual(
    {
        'categorical_column': {
            'class_name': 'SequenceCategoricalColumn',
            'config': {
                'categorical_column': {
                    'class_name': 'IdentityCategoricalColumn',
                    'config': {
                        'default_value': None,
                        'key': 'animal',
                        'number_buckets': 4
                    }
                }
            }
        }
    }, config)

new_animal = fc.IndicatorColumn.from_config(config)
self.assertEqual(animal, new_animal)
self.assertIsNot(parent, new_animal.categorical_column)

new_animal = fc.IndicatorColumn.from_config(
    config,
    columns_by_name={
        serialization._column_name_with_class_name(parent): parent
    })
self.assertEqual(animal, new_animal)
self.assertIs(parent, new_animal.categorical_column)
