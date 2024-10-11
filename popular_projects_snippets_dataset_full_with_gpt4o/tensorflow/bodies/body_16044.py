# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
with self.assertRaisesRegex(ValueError, 'No TypeSpec is compatible'):
    spec1.most_specific_compatible_type(spec2)
