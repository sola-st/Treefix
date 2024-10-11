# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/analyzer_test.py

@tf.function(input_signature=[
    tf.TensorSpec(shape=[1, 100, 512], dtype=tf.float32),
    tf.TensorSpec(shape=[512, 8, 64], dtype=tf.float32)
])
def func(lhs, rhs):
    exit(tf.einsum('ABD,DNH->ABNH', lhs, rhs))

converter = tf.lite.TFLiteConverter.from_concrete_functions(
    [func.get_concrete_function()], func)
fb_model = converter.convert()
mock_stdout = io.StringIO()
with test.mock.patch.object(sys, 'stdout', mock_stdout):
    analyzer.ModelAnalyzer.analyze(model_content=fb_model)
txt = mock_stdout.getvalue()
self.assertIn('Op#0 RESHAPE(T#1, T#4[512, 512]) -> [T#5]', txt)
self.assertIn('Op#1 TRANSPOSE(T#5, T#3[1, 0]) -> [T#6]', txt)
self.assertIn('Op#2 FULLY_CONNECTED(T#0, T#6, T#-1) -> [T#7]', txt)
self.assertIn('Op#3 RESHAPE(T#7, T#2[1, 100, 8, 64]) -> [T#8]', txt)
self.assertIn(
    'T#2(einsum/Einsum) shape:[4], type:INT32 RO 16 bytes, '
    'buffer: 3, data:[1, 100, 8, 64]', txt)
self.assertIn(
    'T#3(einsum/Einsum2) shape:[2], type:INT32 RO 8 bytes, '
    'buffer: 4, data:[1, 0]', txt)
self.assertIn(
    'T#4(einsum/Einsum3) shape:[2], type:INT32 RO 8 bytes, '
    'buffer: 5, data:[512, 512]', txt)
