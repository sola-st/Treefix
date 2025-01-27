# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
with context.graph_mode():
    classes = array_ops.placeholder(dtypes.float32, 1, name='output-tensor-1')
    with self.assertRaisesRegex(
        ValueError, 'Classification classes must be a string Tensor'):
        export_output_lib.ClassificationOutput(classes=classes)
