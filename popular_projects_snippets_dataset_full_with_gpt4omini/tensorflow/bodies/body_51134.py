# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output_test.py
with context.graph_mode():
    scores = array_ops.placeholder(dtypes.string, 1, name='output-tensor-1')
    with self.assertRaisesRegex(
        ValueError, 'Classification scores must be a float32 Tensor'):
        export_output_lib.ClassificationOutput(scores=scores)
