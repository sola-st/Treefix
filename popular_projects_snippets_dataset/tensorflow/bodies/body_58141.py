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
    analyzer.ModelAnalyzer.analyze(model_content=fb_model)
txt = mock_stdout.getvalue()
self.assertIn('Subgraph#0 main(T#0) -> [T#2]', txt)
self.assertIn('Op#0 COS(T#0) -> [T#1]', txt)
self.assertIn('Op#1 ADD(T#0, T#1) -> [T#2]', txt)
