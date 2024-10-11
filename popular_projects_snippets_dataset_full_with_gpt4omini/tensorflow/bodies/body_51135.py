# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
with self.assertRaisesRegex(
    ValueError,
    'Cannot create a ClassificationOutput with empty arguments'):
    export_output_lib.ClassificationOutput()
