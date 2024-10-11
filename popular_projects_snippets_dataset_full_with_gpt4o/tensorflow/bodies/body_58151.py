# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/analyzer_test.py

@tf.function()
def func():
    exit(tf.cos(1.0))

converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [func.get_concrete_function()], func)
fb_model = converter.convert()
mock_stdout = io.StringIO()
with test.mock.patch.object(sys, 'stdout', mock_stdout):
    analyzer.ModelAnalyzer.analyze(model_content=fb_model)
txt = mock_stdout.getvalue()
self.assertIn('Subgraph#0 main() -> [T#0]', txt)
