# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/analyzer_test.py

@tf.function(
    input_signature=[tf.TensorSpec(shape=[None], dtype=tf.float32)])
def func(x):
    exit(x + tf.cos(x))

converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [func.get_concrete_function()], func)
fb_model = converter.convert()
mock_stdout = io.StringIO()
with test.mock.patch.object(sys, 'stdout', mock_stdout):
    analyzer.ModelAnalyzer.analyze(
        model_content=fb_model, gpu_compatibility=True)
txt = mock_stdout.getvalue()
self.assertIn(
    'Your model looks compatible with GPU delegate with TFLite runtime',
    txt)
