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
        model_content=fb_model, experimental_use_mlir=True)
mlir = mock_stdout.getvalue()
self.assertIn('func @main(%arg0: tensor<?xf32>) -> tensor<?xf32>', mlir)
self.assertIn('%0 = "tfl.cos"(%arg0) : (tensor<?xf32>) -> tensor<?xf32>',
              mlir)
self.assertIn(
    '%1 = tfl.add %arg0, %0 {fused_activation_function = "NONE"} : '
    'tensor<?xf32>', mlir)
self.assertIn('return %1 : tensor<?xf32', mlir)
